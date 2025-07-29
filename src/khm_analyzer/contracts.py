from abc import ABC, abstractmethod


class AbstractKHM(ABC):
    pass


class Renderable(AbstractKHM):
    @abstractmethod
    def render(self):
        ...


class AbstractTale(Renderable):
    @property
    @abstractmethod
    def head(self):
        ...

    @property
    @abstractmethod
    def paragraphs(self):
        ...


class AbstractHead(Renderable):
    @property
    @abstractmethod
    def number(self):
        ...

    @property
    @abstractmethod
    def head_text(self):
        ...


class AbstractParagraph(Renderable):
    ...


class AbstractSentence(Renderable):
    ...


class AbstractWord(Renderable):
    ...

