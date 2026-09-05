from itertools import chain

ANY_NAMESPACE = "*"
TEI_NAMESPACE = "http://www.tei-c.org/ns/1.0"
XML_NAMESPACE = "http://www.w3.org/XML/1998/namespace"
EXSLT_NAMESPACE = "http://exslt.org/regular-expressions"

NAMESPACE_MAP = {
    "any": ANY_NAMESPACE,
    "ns": TEI_NAMESPACE,
    "xml": XML_NAMESPACE,
    "exslt": EXSLT_NAMESPACE,
}

parentheses = ("{", "}")
flatten = chain.from_iterable


def any_namespace(tag: str) -> str:
    return "".join(flatten(zip(parentheses, (ANY_NAMESPACE, tag), strict=True)))


def xml_namespace(tag: str) -> str:
    return "".join(flatten(zip(parentheses, (XML_NAMESPACE, tag), strict=True)))


def tei_namespace(tag: str) -> str:
    return "".join(flatten(zip(parentheses, (TEI_NAMESPACE, tag), strict=True)))


def exslt_namespace(tag: str) -> str:
    return "".join(flatten(zip(parentheses, (EXSLT_NAMESPACE, tag), strict=True)))
