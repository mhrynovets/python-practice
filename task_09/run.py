#!/usr/bin/python3
""" append 2nd string in the middle of 1st string """
# 9. Given 2 strings, s1 and s2,
# create a new string by appending s2 in the middle of s1
# (e.g. "Chrisdem", “IamNewString” → "ChrIamNewStringisdem")

import sys


def main():
    """ Main routine """
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} str1 str2")
        print("Exit.")
        sys.exit(1)

    # solution by one line
    # print(sys.argv[1][0:(len(sys.argv[1])//2):]+sys.argv[2]+sys.argv[1][(len(sys.argv[1])//2)::])

    str1 = sys.argv[1]
    str2 = sys.argv[2]
    s1middle = len(str1)//2
    res = str1[0:s1middle:] + str2 + str1[s1middle::]
    print(res)


if __name__ == "__main__":
    main()
