from argparse import Namespace
from lxml import etree
from .. import parser as khm_parser
from ..elements import Tale


def display(args: Namespace) -> None:
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
