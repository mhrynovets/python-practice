#!/usr/bin/python3

# 2. Create script which accepts file name and puts it’s extension to output.
# If there is no extension - exception should be raised.

import sys

if (len(sys.argv) == 1):
    raise Exception('No Filename given')

if len(sys.argv) > 2:
    raise Exception('Wrong arguments given. Filename with spaces should be enclosed in qoutes.')

fname = sys.argv[1].strip("\"'")
dot_pos = fname.rfind(".")

if (dot_pos == -1):
    raise Exception('Got Filename without extension')

if (fname[dot_pos::].find(" ") != -1):
    raise Exception('Got Filename with wrong extension')

print(fname[dot_pos::])

# 20121021.my.file.name.txt.tar.bz2.gpg.part01
# 20121021.my.file.name.txt
# don't found standards - how to find, where to stop discovery of nested extensions,
# so i think, that it should be the last part. Nested containers will have own extensions.
