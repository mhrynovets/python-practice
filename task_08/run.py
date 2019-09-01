#!/usr/bin/python3
""" password generator """
# 8. Write a password generator. Pass password length as a script param
import random
import sys


def main():
    """ Main routine """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} LENGTH")
        print("Exit.")
        sys.exit(1)

    try:
        length = int(sys.argv[1])
    except ValueError:
        print("Got wrong number - exit.")
        sys.exit(1)

    chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"\
        "!@#$%^&*()?"

    password = ""
    for _ in range(length):
        password += chars[random.randint(0, len(chars)-1)]

    print(password)


if __name__ == "__main__":
    main()
