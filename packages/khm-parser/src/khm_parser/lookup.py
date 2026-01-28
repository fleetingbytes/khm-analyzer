from lxml import etree

from khm_parser.utils import get_class_with_dtaid


class Lookup(etree.CustomElementClassLookup):
    def lookup(self, node_type, _document, namespace, name):
        pass_on_to_default_fallback = None
        if node_type == "element":
            cls = get_class_with_dtaid(name, self.DTAID, pass_on_to_default_fallback)
            return cls
        return pass_on_to_default_fallback
