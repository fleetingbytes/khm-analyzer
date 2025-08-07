NAMESPACE_MAP = { "ns": "http://www.tei-c.org/ns/1.0" }
ANY_NAMESPACE = "{*}"
XML_NAMESPACE = "{http://www.w3.org/XML/1998/namespace}"

def any_namespace(tag: str) -> str:
    return "".join((ANY_NAMESPACE, tag))

def xml_namespace(tag: str) -> str:
    return "".join((XML_NAMESPACE, tag))
