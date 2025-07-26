import argparse

parser = argparse.ArgumentParser(
    prog="khm-analyzer",
    description="Parses linguistically annoted editions of Grimm's Fairy Tales",
)

parser.add_argument("source_file", type=argparse.FileType("r", encoding="UTF-8"))

def run() -> None:
    args = parser.parse_args()
    line = next(args.source_file)
    print(line.strip())
