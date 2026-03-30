from collections.abc import Generator
from io import StringIO

from khm_parser.composites import Sentence, Word
from khm_parser.elements import Head, SentencePart, WordPart
from khm_renderer.corrections import Corrections
from khm_renderer.render_functions import RenderFunctions
from khm_renderer.separators import Separators


class KhmRenderer:
    def __init__(
        self,
        render_functions: RenderFunctions | None = None,
        sep: Separators | None = None,
        corrections: Corrections | None = None,
    ) -> None:
        if render_functions is None:
            render_functions = RenderFunctions()
        if sep is None:
            sep = Separators()
        if corrections is None:
            corrections = Corrections()

        self.renderers: RenderFunctions = render_functions
        self.sep: Separators = sep
        self.corrections: Corrections = corrections

    def render_tale_head(self, head: Head, buffer: StringIO) -> StringIO:
        return self.renderers.render_tale_head(head, buffer, self.renderers, self.sep, self.corrections)

    def render_tale_number(self, number: WordPart, buffer: StringIO) -> StringIO:
        return self.renderers.render_tale_number(number, buffer, self.renderers)

    def render_tale_title(self, title: Generator[Sentence], buffer: StringIO) -> StringIO:
        return self.renderers.render_tale_title(title, buffer, self.renderers, self.sep, self.corrections)

    def render_sentence(self, sentence: Sentence, buffer: StringIO) -> StringIO:
        return self.renderers.render_sentence(sentence, buffer, self.renderers, self.sep, self.corrections)

    def render_sentence_part(self, sentence_part: SentencePart, buffer: StringIO) -> StringIO:
        return self.renderers.render_sentence_part(sentence_part, buffer, self.renderers, self.sep)

    def render_word(self, word: Word, buffer: StringIO) -> StringIO:
        return self.renderers.render_word(word, buffer, self.renderers, self.sep)

    def render_word_part(self, word_part: WordPart, buffer: StringIO) -> StringIO:
        rendered_word_part = self.renderers.render_word_part(word_part)
        buffer.write(rendered_word_part)
        return buffer
