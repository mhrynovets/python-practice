#!/usr/bin/python3

# 8. Write a password generator. Pass password length as a script param
import random

length = 16
chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = ""
for i in range(length):
    password += chars[random.randint(0, len(chars)-1)]

print(password)
