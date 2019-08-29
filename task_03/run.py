#!/usr/bin/python3

# 3. Create script which accepts directory name
# and puts list of files in this directory to output.

import sys
import os

if (len(sys.argv) != 2):
    print("Usage: %s DIRNAME\nExiting..." % sys.argv[0])
    sys.exit(1)

dirName = sys.argv[1]
try:
    items = os.listdir(dirName)
except:
    print("Wrong DIRNAME is typed or directory not exist.")
    sys.exit(1)

for name in items:
    if os.path.isfile(os.path.join(dirName, name)):
        print(name)
