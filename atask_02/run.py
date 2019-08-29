#!/usr/bin/python3

# 2. Write a program that accepts a sequence of comma separated words as input 
# and prints the words 
# after removing all duplicate words 
# and sorting them alphanumerically. 
# Suppose the following input is supplied to the program: 
# hello world and practice makes perfect and hello world again. 
# Then, the output should be: 
# again and hello makes perfect practice world.

import sys

if (len(sys.argv) != 2):
    print("Usage: %s STR where STR - comma separated words" % sys.argv[0])
    print("Exit.")
    sys.exit(1)


separator = ','
words = sys.argv[1]

wordsSeparated = words.split(separator)
wordsSeparatedUniq = list(set(wordsSeparated))
wordsSeparatedUniqSorted = sorted(wordsSeparatedUniq)

print(wordsSeparated)
print(wordsSeparatedUniqSorted)
