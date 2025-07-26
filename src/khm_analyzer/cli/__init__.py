import argparse
from .. import parser as khm_parser

arg_parser = argparse.ArgumentParser(
    prog="khm-analyzer",
    description="Parses linguistically annoted editions of Grimm's Fairy Tales",
)

arg_parser.add_argument("source_file", type=argparse.FileType("r", encoding="UTF-8"))

def run() -> None:
    args = arg_parser.parse_args()
    khm_parser.parse(args.source_file)
