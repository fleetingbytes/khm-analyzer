from abc import ABC, abstractmethod


class AbstractKHM(ABC):
    pass


class Renderable(AbstractKHM):
    @abstractmethod
    def render(self) -> str:
        ...


class AbstractTale(Renderable):
    @abstractmethod
    def metadata(self, number: bool, title: bool) -> str:
        ...

    @abstractmethod
    def render(self, number: bool, title: bool, one_sentence_per_line: bool) -> str:
        ...



class AbstractHead(Renderable):
    @property
    @abstractmethod
    def number(self):
        ...


class AbstractParagraph(Renderable):
    @abstractmethod
    def render(self, sentence_separator: str) -> str:
        ...


class AbstractSentence(Renderable):
    ...


class AbstractWord(Renderable):
    ...

