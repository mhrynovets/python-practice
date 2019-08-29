#!/usr/bin/python3

# 1. Write a program, which will count spaces, tabs and new lines in file. 
# File path should be passed as a script argument. Check if file exists before reading it.

import re, sys

if (len(sys.argv) != 2):
    print("Usage: %s FILE" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        text = f.read()
except:
    print("Can't read given file. Exiting...")
    sys.exit(1)

found = re.findall(r"([\t\n\ ]{1})", text)
print("There are such count of tab, space and new-line characters:",len(found))