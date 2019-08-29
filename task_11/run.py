#!/usr/bin/python3

# 11. Create script, which reads n random lines from file1 and appends them to file2. 
# Pass n, file1, file2 as script parameters.

import sys
import random

if (len(sys.argv) != 4):
    print("Usage: %s COUNT, FILE1, FILE2" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    count = int(sys.argv[1])
except:
    print("Typed wrong COUNT parameter. Exit.")
    sys.exit(1)    

try:
    with open(sys.argv[2]) as f:
        lines = f.readlines()
except:
    print("Can't read first file. Exit.")
    sys.exit(1)

try:
    with open(sys.argv[3], 'a') as f:
        for n in range(int(sys.argv[1])):
            f.write(random.choice(lines))
except:
    print("Can't write second file. Exit.")
    sys.exit(1)