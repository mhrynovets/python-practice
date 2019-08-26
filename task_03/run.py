#!/usr/bin/python3

# 3. Create script which accepts directory name
# and puts list of files in this directory to output.

import sys
import os

if (len(sys.argv) == 1):
    raise Exception('No Directory name given')

dirName = sys.argv[1]

items = os.listdir(dirName)
for name in items:
    if os.path.isfile(os.path.join(dirName, name)):
        print(name)
