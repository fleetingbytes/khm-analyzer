import argparse
from lxml import etree
from .. import parser as khm_parser

arg_parser = argparse.ArgumentParser(
    prog="khm-analyzer",
    description="Parses linguistically annoted editions of Grimm's Fairy Tales",
)

arg_parser.add_argument("source_file", type=argparse.FileType("r", encoding="UTF-8"))
arg_parser.add_argument("tale", type=int)

def run() -> None:
    args = arg_parser.parse_args()
    root: etree.Element = khm_parser.parse(args.source_file)
    tale: etree.Element = khm_parser.get_fairy_tale(root, args.tale)
