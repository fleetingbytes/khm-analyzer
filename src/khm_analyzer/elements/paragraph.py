from ..bases import ParagraphBase, SentencePartBase, LineGroupBase
from ..namespace import NAMESPACE_MAP
from collections.abc import Iterable
from io import StringIO
from string import whitespace


class Paragraph(ParagraphBase):
    @property
    def sentences_and_linegroups(self) -> Iterable[SentencePartBase | LineGroupBase]:
        xpath = ".//ns:s[not(ancestor::ns:lg)] | .//ns:lg"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

    def render(self, sentence_separator: str, **kwargs) -> str:
        buffer = StringIO()
        start_of_trailing_space_after_last_element: int = buffer.tell()

        for sentence_or_linegroup in self.sentences_and_linegroups:
            if isinstance(sentence_or_linegroup, SentencePartBase):
                sentence = sentence_or_linegroup
                start_of_trailing_space_after_last_element = self.write_element(sentence, sentence_separator, buffer)
                buffer = self.add_space_after_sentence(sentence, sentence_separator, buffer)
            else:
                linegroup = sentence_or_linegroup
                buffer = self.create_or_adjust_space_before_linegroup(start_of_trailing_space_after_last_element, buffer)
                start_of_trailing_space_after_last_element = self.write_element(linegroup, sentence_separator, buffer)
                buffer = self.add_space_after_linegroup(buffer)

        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)

        return buffer.getvalue()

    def create_or_adjust_space_before_linegroup(self, start_of_trailing_space_after_last_element: int, buffer: StringIO) -> StringIO:
        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)
        buffer.write("\n\n")
        return buffer

    def add_space_after_linegroup(self, buffer: StringIO) -> StringIO:
        buffer.write("\n\n")
        return buffer
