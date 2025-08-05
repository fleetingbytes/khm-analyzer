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

def render_tale_number_or_title(tale: Tale, args: argparse.ArgumentParser) -> None:
    if args.include_tale_number:
        print(f"{tale.number}.")
    if args.include_tale_title:
        print(tale.render_head())
    if args.include_tale_number or args.include_tale_title:
        print()


def run() -> None:
    args = arg_parser.parse_args()
    root: etree.Element = khm_parser.parse(args.source_file)
    tale: Tale = khm_parser.get_fairy_tale(root, args.tale)
    print(
        tale.render(
            number=args.include_tale_number,
            title=args.include_tale_title,
            one_sentence_per_line=args.one_sentence_per_line,
        )
    )
