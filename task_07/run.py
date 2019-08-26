#!/usr/bin/python3

# 7. Create script, which will read random line from file (file will pass as parameter),
# print line to output and count letters in that line.

import sys
import random
import re

if (len(sys.argv) == 1):
    print("You should type a filename as parameter!")
    sys.exit(1)

with open(sys.argv[1]) as f:
    lines = f.readlines()

randLine = random.choice(lines).strip()
print(randLine)

letters = re.findall(r"([a-zA-Z])", randLine)
print("This line contains:", len(letters), "letters")
