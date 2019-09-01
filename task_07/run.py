#!/usr/bin/python3
""" print random line from file and count letters in that line """
# 7. Create script, which will read random line from file
# (file will pass as parameter),
# print line to output and count letters in that line.

import sys
import random
import re
import os


def main():
    """ Main routine random line"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} FILE")
        print("Exit.")
        sys.exit(1)

    if not os.path.isfile(sys.argv[1]) and not os.access(sys.argv[1], os.R_OK):
        print("Typed JSON file not found or no permissions to access. Exit.")
        sys.exit(1)

    with open(sys.argv[1]) as read_file:
        lines = read_file.readlines()

    rand_line = random.choice(lines).strip()
    print(rand_line)

    letters = re.findall(r"([a-zA-Z])", rand_line)
    print("This line contains:", len(letters), "letters")


if __name__ == "__main__":
    main()
