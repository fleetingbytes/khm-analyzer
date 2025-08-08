from itertools import chain


ANY_NAMESPACE = "*"
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0" 
XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"

NAMESPACE_MAP = { "ns": TEI_NAMESPACE }

parentheses = ("{", "}")

def any_namespace(tag: str) -> str:
    return "".join(chain.from_iterable(zip(parentheses, (ANY_NAMESPACE, tag), strict=True)))

def xml_namespace(tag: str) -> str:
    return "".join(chain.from_iterable(zip(parentheses, (XML_NAMESPACE, tag), strict=True)))

def tei_namespace(tag: str) -> str:
    return "".join(chain.from_iterable(zip(parentheses, (TEI_NAMESPACE, tag), strict=True)))
