#!/usr/bin/python3

# 11. Create script, which reads n random lines from file1 and appends them to file2. 
# Pass n, file1, file2 as script parameters.

import sys
import random

if (len(sys.argv) != 4):
    print("You should type COUNT, FILE1, FILE2 as script parameters")
    sys.exit(1)

with open(sys.argv[2]) as f:
    lines = f.readlines()

with open(sys.argv[3], 'a') as f:
    for n in range(int(sys.argv[1])):
        f.write(random.choice(lines))
