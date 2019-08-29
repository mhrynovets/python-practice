#!/usr/bin/python3

# 7. Create script, which will read random line from file (file will pass as parameter),
# print line to output and count letters in that line.

import sys
import random
import re

if (len(sys.argv) != 2):
    print("Usage: %s FILE" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        lines = f.readlines()
except:
    print("Can't read given file. Exiting...")
    sys.exit(1)

randLine = random.choice(lines).strip()
print(randLine)

letters = re.findall(r"([a-zA-Z])", randLine)
print("This line contains:", len(letters), "letters")
