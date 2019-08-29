#!/usr/bin/python3

# 9. Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
# (e.g. "Chrisdem", “IamNewString” → "ChrIamNewStringisdem")

import sys

if (len(sys.argv) != 3):
    print("Usage: %s str1 str2" % sys.argv[0])
    print("Exit.")
    sys.exit(1)
    
# solution by one line
# print(sys.argv[1][0:(len(sys.argv[1])//2):]+sys.argv[2]+sys.argv[1][(len(sys.argv[1])//2)::])

s1 = sys.argv[1]
s2 = sys.argv[2]
s1middle = len(s1)//2
res = s1[0:s1middle:] + s2 + s1[s1middle::]
print(res)
