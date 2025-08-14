import argparse
from lxml import etree
from .. import parser as khm_parser
from ..elements import Tale

arg_parser = argparse.ArgumentParser(
    prog="khm-analyzer",
    description="Parses linguistically annotated editions of Grimm's Fairy Tales",
)

arg_parser.add_argument("source_file", type=argparse.FileType("r", encoding="UTF-8"))
arg_parser.add_argument("tale", type=int)
arg_parser.add_argument("-n", "--include-tale-number", action="store_true")
arg_parser.add_argument("-t", "--include-tale-title", action="store_true")
arg_parser.add_argument("-s", "--one-sentence-per-line", action="store_true")

def run() -> None:
    args = arg_parser.parse_args()

    source_file = args.source_file
    tale_number = args.tale

    root: etree.Element = khm_parser.parse(source_file)
    tale: Tale = khm_parser.get_fairy_tale(root, tale_number)

    kwargs = {
        "number": args.include_tale_number,
        "title": args.include_tale_title,
        "one_sentence_per_line": args.one_sentence_per_line,
    }

    print(tale.render(**kwargs))
