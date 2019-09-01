#!/usr/bin/python3
""" List files in given directory """
# 3. Create script which accepts directory name
# and puts list of files in this directory to output.

import sys
import os


def main():
    """ Main routine """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} DIRNAME\nExit.")
        sys.exit(1)

    dir_name = sys.argv[1]

    if not os.path.isdir(dir_name):
        print(f"Destination path '{dir_name}' is not valid directory. "
              "Exit.")
        sys.exit(1)
    if not os.access(dir_name, os.R_OK):
        print(f"Can not access destination directory '{dir_name}'. "
              "Exit.")
        sys.exit(1)

    items = os.listdir(dir_name)
    for name in items:
        if os.path.isfile(os.path.join(dir_name, name)):
            print(name)


if __name__ == "__main__":
    main()
