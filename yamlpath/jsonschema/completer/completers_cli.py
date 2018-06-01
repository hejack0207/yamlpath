from __future__ import absolute_import
import argparse
import json
import sys

def _json_file(path):
    with open(path) as file:
        return json.load(file)


parser = argparse.ArgumentParser(
    description="JSON Schema Completion CLI",
)
parser.add_argument(
    "schema",
    help="the JSON Schema to complete with (i.e. filename.schema)",
    type=_json_file,
)


def parse_args(args):
    arguments = vars(parser.parse_args(args=args or ["--help"]))
    return arguments


def main(args=sys.argv[1:]):
    sys.exit(run(arguments=parse_args(args=args)))


def run(arguments, stdout=sys.stdout, stderr=sys.stderr):
    schema=arguments["schema"]

    return 0

if __name__ == "__main__":
    main()
