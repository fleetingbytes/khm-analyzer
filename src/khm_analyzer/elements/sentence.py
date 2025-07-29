from ..bases import SentenceBase, WordBase


class Sentence(SentenceBase):
    def render(self) -> str:
        sentence = "".join(word.render() for word in self.iterdescendants(tag=WordBase.TAG))
        return sentence.strip()
