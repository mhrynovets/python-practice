#!/usr/bin/python3
""" Count lines, that contain 'is' and 'the' in text of given URL """

# 4. For the given url, count the total number of lines
# that contain 'is' or 'the' as whole words.
# Note, that each line in the for loop will be of bytes data type.
# Use urllib or requests lib.
# (https://www.gutenberg.org/cache/epub/60/pg60.txt)

import re
import urllib.request
import sys
import argparse


def main():
    """ Main routine """
    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                        help='URL with text, where to find '
                             'lines with keywords')
    parser.add_argument('-f', '--find', nargs='?', action='append',
                        help='Which keyword to search in text. Flag can be '
                        'used multiple times to search many keywords.')
    args = parser.parse_args()

    if args.url.find("://") == -1:
        print("URL should contain protocol prefix "
              "( http://, https://, etc. ). Exit. ")
        sys.exit(1)

    try:
        with urllib.request.urlopen(args.url) as response:
            encoding = response.info().get_param('charset', 'utf8')
            html = response.read().decode(encoding)
    except urllib.error.URLError as err:
        print(f"Error occurred: {err.reason.strerror}. Exit.")
        sys.exit(1)
    except ValueError:
        print("Typed wrong URL. Exit.")
        sys.exit(1)

    lines = html.splitlines()

    if args.find:
        words = "|".join(set(args.find))
    else:
        words = "is|the"

    found = []
    for line in lines:
        regex = re.findall(r'((?:\W|^)(?:'+words+r')(?:\W|$))', line)
        if regex:
            found.append(regex)

    if found:
        print("Text contains {} lines, where words '{}' are included as whole "
              "word.".format(len(found), "', '".join(set(args.find))))


if __name__ == "__main__":
    main()
