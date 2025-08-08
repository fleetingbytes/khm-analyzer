from lxml import etree
from .elements import get_class_with_dtaid


class Lookup(etree.CustomElementClassLookup):
    def lookup(self, node_type, _document, namespace, name):
        PASS_ON_TO_DEFAULT_FALLBACK = None
        if node_type == "element":
            cls = get_class_with_dtaid(name, self.DTAID, PASS_ON_TO_DEFAULT_FALLBACK)
            return cls
        return PASS_ON_TO_DEFAULT_FALLBACK
