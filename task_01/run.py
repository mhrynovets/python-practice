#!/usr/bin/python3
""" builds Pascal triangle with n rows """
# 1. Create script which builds Pascal triangle with n rows.
# Script accepts n as argument.
import sys


def main():
    """ Main routine """
    try:
        if len(sys.argv) == 2:
            count = int(sys.argv[1])
        else:
            count = int(input("Enter number of rows: ") or 3)
    except ValueError:
        print("You typed a wrong number. Showing 3 rows as demo.")
        count = 3

    rows = []
    for i in range(count):
        rows.append([])
        rows[i].append(1)
        for j in range(1, i):
            rows[i].append(rows[i-1][j-1]+rows[i-1][j])
        if i != 0:
            rows[i].append(1)

    for row in range(len(rows)):
        print(", ".join([str(x) for x in rows[row]]))


if __name__ == "__main__":
    main()
