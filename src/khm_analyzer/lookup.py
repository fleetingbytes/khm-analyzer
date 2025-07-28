from lxml import etree
from .elements import ELEMENTS_MAP


class Lookup(etree.CustomElementClassLookup):
    def lookup(self, node_type, _document, namespace, name):
        PASS_ON_TO_DEFAULT_FALLBACK = None
        if node_type == "element":
            return ELEMENTS_MAP.get(name, PASS_ON_TO_DEFAULT_FALLBACK)
        return PASS_ON_TO_DEFAULT_FALLBACK
