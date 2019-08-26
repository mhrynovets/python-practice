#!/usr/bin/python3

# 4. Write a program that takes text and prints two words: the most common and the longest.

import sys
import string

text = ""

# read file, given as argument
if (len(sys.argv) > 1):
    with open(sys.argv[1]) as f:
        for line in f:
            text += line
# or read piped incomming text 
else:
    for line in sys.stdin:
        text += line

words = [word.strip(string.punctuation) for word in text.split()]

used = {}
longest = ""

for item in words:
    if (len(longest) < len(item)):
        longest = item
    if item in used:
        used[item] += 1
    else:
        used[item] = 1

most_common = max(used, key=used.get)

print("Longest word is: ", longest)
print("Most common used word is: %s (%s times used)." % (most_common,used[most_common]))
