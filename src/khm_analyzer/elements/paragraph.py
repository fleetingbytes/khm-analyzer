from ..bases import ParagraphBase, SentenceBase, LineGroupBase
from ..namespace import NAMESPACE_MAP
from collections.abc import Iterable
from io import StringIO
from string import whitespace


class Paragraph(ParagraphBase):
    @property
    def sentences(self) -> Iterable[SentenceBase]:
        yield from self.iterdescendants(tag=SentenceBase.TAG)

    @property
    def sentences_and_linegroups(self) -> Iterable[SentenceBase | LineGroupBase]:
        xpath = ".//ns:s[not(ancestor::ns:lg)] | .//ns:lg"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

    def render(self, sentence_separator: str) -> str:
        buffer = StringIO()
        start_of_trailing_space_after_last_element: int = buffer.tell()

        for sentence_or_linegroup in self.sentences_and_linegroups:
            if isinstance(sentence_or_linegroup, SentenceBase):
                sentence = sentence_or_linegroup
                start_of_trailing_space_after_last_element = self.write_element(sentence, buffer)
                buffer = self.add_space_after_sentence(sentence, sentence_separator, buffer)
            else:
                linegroup = sentence_or_linegroup
                buffer = self.create_or_adjust_space_before_linegroup(start_of_trailing_space_after_last_element, buffer)
                start_of_trailing_space_after_last_element = self.write_element(linegroup, buffer)
                buffer = self.add_space_after_linegroup(linegroup, buffer)

        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)

        return buffer.getvalue()

    def write_element(self, element: SentenceBase | LineGroupBase, buffer: StringIO) -> int:
        buffer.write(element.render())
        cookie = buffer.tell()
        return cookie

    def add_space_after_sentence(self, sentence: SentenceBase, separator: str, buffer: StringIO) -> StringIO:
        if not sentence.has_a_following_part:
            buffer.write(separator)
        return buffer

    def create_or_adjust_space_before_linegroup(self, start_of_trailing_space_after_last_element: int, buffer: StringIO) -> StringIO:
        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)
        buffer.write("\n\n")
        return buffer

    def add_space_after_linegroup(self, linegroup: LineGroupBase, buffer: StringIO) -> StringIO:
        buffer.write("\n\n")
        return buffer

    def strip_trailing_space(self, start_of_trailing_space_after_last_element, buffer: StringIO) -> StringIO:
        buffer.seek(start_of_trailing_space_after_last_element)
        buffer.truncate()
        return buffer
