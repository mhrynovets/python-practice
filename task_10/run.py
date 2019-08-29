#!/usr/bin/python3

# 10. Given a following two sets find the intersection and remove those elements from the first set. 
# Print first set before removing, removed elements and first set after removing elements.

# fruits = {"apple", "banana", "cherry", "dog", "grape", "lemon", "orange", "monkey"}
# animals = {"dog", "cow", "cat", "monkey", "rabbit"}
import sys

if len(sys.argv) not in range(2,4):
    print("Usage: %s FILE1 FILE2. Exiting..." % sys.argv[0])
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        line = f.readline()
        fruits = {x.strip(" ").strip("'\"") for x in line.split(",")}
except:
    print("Can't read first file. Exiting...")
    sys.exit(1)

try:
    with open(sys.argv[2]) as f:
        line = f.readline()
        animals = {x.strip(" ").strip("'\"") for x in line.split(",")}
except:
    print("Can't read second file. Exiting...")
    sys.exit(2)

print("Defined set of fruits:", fruits)
print("Defined set of animals:", animals)
print("Intersection between defined sets 'fruits' and 'animals':",fruits.intersection(animals))
print("Removing intersected items from 'fruits'",fruits.intersection(animals)); fruits.difference_update(animals)
print("Final set of 'fruits'",fruits)