#!/usr/bin/python3
""" count occurrences of all characters within a string """
# 12. Given an input string,
# count occurrences of all characters within a string
# (e.g. pythonnohtyppy -> p:3, y:3, t:2, h:2, o:2, n:2)

import sys


def main():
    """ Main routine """
    if len(sys.argv) != 2:
        print("You should type one word, if spaces are present - string "
              "must be enclosed in quotes")
        sys.exit(1)

    word = sys.argv[1].strip("\"'")

    used = {}

    for item in word:
        if item in used:
            used[item] += 1
        else:
            used[item] = 1

    used_sort = dict(sorted(used.items(), key=lambda item: item[1],
                            reverse=True))

    print(word, "->", ", ".join([k+":"+str(v) for k, v in used_sort.items()]))


if __name__ == "__main__":
    main()
