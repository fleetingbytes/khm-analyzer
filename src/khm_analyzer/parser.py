import xml.etree.ElementTree as ET
from io import TextIOWrapper


def parse(fd: TextIOWrapper) -> None:
    tree = ET.parse(fd)
    root = tree.getroot()
    namespace = { "ns": "http://www.tei-c.org/ns/1.0" }
    text = root.find("ns:text", namespace)
    breakpoint()
