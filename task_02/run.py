#!/usr/bin/python3

# 2. Create script which accepts file name and puts it’s extension to output.
# If there is no extension - exception should be raised.

import sys

if (len(sys.argv) != 2):
    raise Exception('No Filename given')

dot_pos = sys.argv[1].rfind(".")

if (sys.argv[1].rfind(".") == -1):
    raise Exception('Got Filename without extension')

if (sys.argv[1][dot_pos::].find(" ") != -1):
    raise Exception('Got Filename with wrong extension')

print(sys.argv[1][dot_pos:])
