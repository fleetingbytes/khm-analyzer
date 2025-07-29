NAMESPACE_MAP = { "ns": "http://www.tei-c.org/ns/1.0" }
ANY_NAMESPACE = "{*}"

def any_namespace(tag: str) -> str:
    return "".join((ANY_NAMESPACE, tag))
