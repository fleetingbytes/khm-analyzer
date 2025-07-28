from ..bases import HeadBase


class Head(HeadBase):
    @property
    def number(self) -> int:
        return 42

    @property
    def head_text(self) -> str:
        return "something"
