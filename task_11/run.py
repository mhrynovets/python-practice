#!/usr/bin/python3
""" Append N random lines from file1 to file2 """
# 11. Create script, which reads n random lines from file1
# and appends them to file2.
# Pass n, file1, file2 as script parameters.

import sys
import random
import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int,
                        help='Count of random lines to read')
    parser.add_argument('infile', type=argparse.FileType('r'),
                        help='Source of random lines')
    parser.add_argument('outfile', type=argparse.FileType('a'),
                        help='Destination to append random lines')
    args = parser.parse_args()

    lines = args.infile.readlines()

    try:
        for _ in range(args.n):
            args.outfile.write(random.choice(lines))
    except OSError as err:
        print(f"Another error occurred: {err.strerror}. Exit.")
        sys.exit(1)


if __name__ == "__main__":
    main()
