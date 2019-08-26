#!/usr/bin/python3

# 4. For the given url, count the total number of lines that contain 'is' or 'the' as whole words.
# Note, that each line in the for loop will be of bytes data type. Use urllib or requests lib.
# (https://www.gutenberg.org/cache/epub/60/pg60.txt)


import re
import urllib.request

url = 'https://www.gutenberg.org/cache/epub/60/pg60.txt'

with urllib.request.urlopen(url) as response:
    encoding = response.info().get_param('charset', 'utf8')
    html = response.read().decode(encoding)

lines = html.splitlines()

found = []
i = 1
for line in lines:
    x = re.findall(r'((?:\W|^)(?:is|the)(?:\W|$))', line)
    if x:
        found.append(x)
        # print(i,":",line)
    i += 1

if found:
    print("Text contains %s lines, where words 'is' or 'the' are included as whole word." % len(found))
