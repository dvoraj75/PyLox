import argparse
import logging
import os
import sys

from scanner import Scanner


def report_error(line_number: int, message: str) -> None:
    logging.error(f"[line: {line_number}] Error: {message}")


def run(source: str) -> None:
    tokens = Scanner(source).scan_tokens()

    for token in tokens:
        print(token)


def run_file(file_path: str) -> int:
    with open(file_path) as f:
        run(f.read())
    return os.EX_OK


def run_prompt():
    while True:
        try:
            line = input(">>> ")
        except EOFError:
            print("")
            break
        run(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Lox interpreter")
    parser.add_argument("lox_file", nargs="?", help="Lox source code file")
    args = parser.parse_args()

    if args.lox_file:
        if os.path.isfile(args.lox_file):
            sys.exit(run_file(args.lox_file))
        logging.error(f"File '{args.lox_file}' does not exist.")
        sys.exit(os.EX_NOINPUT)
    else:
        run_prompt()
