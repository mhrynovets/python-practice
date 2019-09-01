#!/usr/bin/python3
""" Remove duplicate from a list """
# 13. Remove duplicate from a list
# and create a tuple and find the minimum and maximum number.
import sys
import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', nargs='?', action='append',
                        help='Items list. Can be used multiple '
                             'times to search many symbols.')

    args = parser.parse_args()
    if not args.list:
        print("No items given. Exit.")
        parser.print_help()
        sys.exit(1)

    print("Defined list: ", args.list)

    uniq_items = []
    for item in args.list:
        if item not in uniq_items and item:
            uniq_items.append(item)
    print("Same list without duplicates:", uniq_items)

    are_digits = [val.lstrip("-+").isdigit() for val in uniq_items]
    if all(are_digits):
        tupl = (min(uniq_items), max(uniq_items))
        print("Tuple with min and max:", tupl)
    else:
        len_items = [len(val) for val in uniq_items]
        tupl = (min(len_items), max(len_items))
        print("Tuple with min and max:", tupl)


if __name__ == "__main__":
    main()
