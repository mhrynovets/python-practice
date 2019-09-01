#!/usr/bin/python3
""" remove elements of 2nd set from 1st set """
# 10. Given a following two sets find the intersection
# and remove those elements from the first set.
# Print first set before removing, removed elements
# and first set after removing elements.

# fruits = {"apple","banana","cherry","dog","grape","lemon","orange","monkey"}
# animals = {"dog","cow","cat","monkey","rabbit"}
import sys
import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--firstset', nargs='?', action='append',
                        help='Elements of first set. Flag can be '
                        'used multiple times to search many keywords.')
    parser.add_argument('-s', '--secondset', nargs='?', action='append',
                        help='Elements of second set. Flag can be '
                        'used multiple times to search many keywords.')
    args = parser.parse_args()

    if not args.firstset and not args.secondset:
        print("No elements given.")
        parser.print_help()
        sys.exit(1)
    print(args.firstset)
    print(args.secondset)
    if args.firstset:
        first = set(args.firstset)
    else:
        first = set({})
    if args.secondset:
        second = set(args.secondset)
    else:
        second = set({})

    print("Defined set #1:", first)
    print("Defined set #2:", second)
    print("Intersection between defined sets :", first.intersection(second))
    print("Removing intersected items from set #1", first.intersection(second))
    first.difference_update(second)
    print("Final set of #1", first)


if __name__ == "__main__":
    main()
