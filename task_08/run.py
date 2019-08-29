#!/usr/bin/python3

# 8. Write a password generator. Pass password length as a script param
import random
import sys

if (len(sys.argv) != 2):
    print("Usage: %s LENGTH" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    length = int(sys.argv[1])
except:
    print("Got wrong number - exit.")
    sys.exit(1)

chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = ""
for i in range(length):
    password += chars[random.randint(0, len(chars)-1)]

print(password)
