#!/usr/bin/python3
""" Program accetps comma separated words,
removes duplicate words and sort words """
# 2. Write a program that accepts a sequence of comma separated words as input
# and prints the words
# after removing all duplicate words
# and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again.
# Then, the output should be:
# again and hello makes perfect practice world.

import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('words', nargs='+', type=str,
                        help='Words, separated with separator')
    parser.add_argument('-s', '--separator', default=",")
    args = parser.parse_args()

    separator = args.separator
    words = " ".join(args.words)

    words_separated = words.split(separator)
    words_separated_uniq = list(set(words_separated))
    words_separated_uniq_sorted = sorted(words_separated_uniq)

    print(separator.join(words_separated))
    print(separator.join(words_separated_uniq_sorted))


if __name__ == "__main__":
    main()
