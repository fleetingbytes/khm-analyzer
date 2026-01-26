from __future__ import annotations

from io import StringIO
from typing import TYPE_CHECKING

from khm_parser.bases import ParagraphBase
from khm_parser.composites.sentence import Sentence
from khm_parser.namespace import NAMESPACE_MAP

if TYPE_CHECKING:
    from collections.abc import Iterable

    from khm_parser.elements.linegroup import LineGroup


class Paragraph(ParagraphBase):
    @property
    def sentences_and_linegroups(self) -> Iterable[Sentence | LineGroup]:
        xpath = ".//ns:s[not(ancestor::ns:lg)] | .//ns:lg"
        yield from self.xpath(xpath, namespaces=NAMESPACE_MAP)

    def render(self, sentence_separator: str, **kwargs) -> str:
        buffer = StringIO()
        start_of_trailing_space_after_last_element: int = buffer.tell()

        for sentence_or_linegroup in self.sentences_and_linegroups:
            if isinstance(sentence_or_linegroup, Sentence):
                sentence = sentence_or_linegroup
                start_of_trailing_space_after_last_element = self.write_element(
                    sentence, sentence_separator, buffer
                )
                buffer = self.add_space_after_sentence(sentence, sentence_separator, buffer)
            else:
                linegroup = sentence_or_linegroup
                buffer = self.create_or_adjust_space_before_linegroup(
                    start_of_trailing_space_after_last_element, buffer
                )
                start_of_trailing_space_after_last_element = self.write_element(
                    linegroup, sentence_separator, buffer
                )
                buffer = self.add_space_after_linegroup(buffer)

        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)

        return buffer.getvalue()

    def create_or_adjust_space_before_linegroup(
        self, start_of_trailing_space_after_last_element: int, buffer: StringIO
    ) -> StringIO:
        buffer = self.strip_trailing_space(start_of_trailing_space_after_last_element, buffer)
        buffer.write("\n\n")
        return buffer

    @staticmethod
    def add_space_after_linegroup(buffer: StringIO) -> StringIO:
        buffer.write("\n\n")
        return buffer
