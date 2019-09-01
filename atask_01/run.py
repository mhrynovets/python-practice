#!/usr/bin/env python3
""" Program, which will count spaces, tabs and new lines in file """

# 1. Write a program, which will count spaces, tabs and new lines in file.
# File path should be passed as a script argument.
# Check if file exists before reading it.

import re
import sys
import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?',
                        help='File, where to count symbols')
    parser.add_argument('-f', '--find', nargs='?', action='append',
                        help='Which symbol to search in text. Can be '
                             'used multiple times to search many symbols.')
    args = parser.parse_args()
    try:
        if args.infile:
            with open(args.infile) as in_file:
                text = in_file.read()
        elif not sys.stdin.isatty():
            text = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(2)
    except PermissionError:
        print("No permissions to acces typed file. Exit.")
        sys.exit(1)
    except FileNotFoundError:
        print("Typed file not found. Exit.")
        sys.exit(1)
    except OSError as err:
        print(f"Another error occurred: {err.strerror}. Exit.")
        sys.exit(1)
    if args.find:
        chars = [x.encode().decode('unicode_escape')
                 for x in set(args.find) if x]
    else:
        chars = ['\t', '\n', ' ']
    found = re.findall("([" + ''.join(chars) + "]{1})", text)
    print("In file found {} occurrences searching of such "
          "characters: {}".format(
              len(found), ', '.join([repr(x) for x in chars]))
          )


if __name__ == "__main__":
    main()
