from abc import ABC, abstractmethod


class AbstractKHM(ABC):
    pass


class AbstractTale(AbstractKHM):
    @property
    @abstractmethod
    def head(self):
        ...

    @property
    @abstractmethod
    def paragraphs(self):
        ...


class AbstractHead(AbstractKHM):
    @property
    @abstractmethod
    def number(self):
        ...

    @property
    @abstractmethod
    def head_text(self):
        ...
