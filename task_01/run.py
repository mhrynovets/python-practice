#!/usr/bin/python3

# 1. Create script which builds Pascal triangle with n rows. Script accepts n as argument.
import sys

try:
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = int(input("Enter number of rows: ") or 3)
except ValueError as err:
    print("You typed a wrong number. Showing 3 rows as demo.")
    n = 3

a = []
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1, i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if (i != 0):
        a[i].append(1)

for row in range(len(a)):
    print(", ".join([str(x) for x in a[row]]))
