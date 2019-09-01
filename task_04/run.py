#!/usr/bin/python3
""" Finds most common and the longest word in
 given file or piped text """
# 4. Write a program that takes text
# and prints two words: the most common and the longest.

import sys
import string
import argparse


def main():
    """ Main routine longest word"""
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', nargs='?',
                        help='File, that contains words')
    args = parser.parse_args()

    try:
        if args.infile:
            with open(args.infile) as read_file:
                text = read_file.read()
        elif not sys.stdin.isatty():
            text = sys.stdin.read()
        else:
            parser.print_help()
            sys.exit(1)
    except FileNotFoundError:
        print("Typed file not exist. Exit.")
        sys.exit(1)
    except PermissionError:
        print("No permissions to acces typed file. Exit.")
        sys.exit(1)
    except OSError as err:
        print(f"Another error occurred: {err.strerror}. Exit.")
        sys.exit(1)

    words = [word.strip(string.punctuation) for word in text.split()]

    used = {}
    longest = ""

    for item in words:
        if len(longest) < len(item):
            longest = item
        if item in used:
            used[item] += 1
        else:
            used[item] = 1

    most_common = max(used, key=used.get)

    print("Longest word is: ", longest)
    print("Most common used word is: {} ({} times used)."
          "".format(most_common, used[most_common]))


if __name__ == "__main__":
    main()
