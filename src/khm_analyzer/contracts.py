from abc import ABC, abstractmethod


class AbstractKHM(ABC):
    pass


class Renderable(AbstractKHM):
    @abstractmethod
    def render(self):
        ...


class AbstractTale(Renderable):
    @abstractmethod
    def metadata(self, number: bool, title: bool) -> str:
        ...

    @abstractmethod
    def render(self, number: bool, title: bool) -> str:
        ...



class AbstractHead(Renderable):
    @property
    @abstractmethod
    def number(self):
        ...


class AbstractParagraph(Renderable):
    ...


class AbstractSentence(Renderable):
    ...


class AbstractWord(Renderable):
    ...

