#!/usr/bin/python3

# 10. Given a following two sets find the intersection and remove those elements from the first set. 
# Print first set before removing, removed elements and first set after removing elements.

fruits = {"apple", "banana", "cherry", "dog", "grape", "lemon", "orange", "monkey"}
animals = {"dog", "cow", "cat", "monkey", "rabbit"}

print("Defined set of fruits:", fruits)
print("Defined set of animals:", animals)
print("Intersection between defined sets 'fruits' and 'animals':",fruits.intersection(animals))
print("Removing intersected items from 'fruits'",fruits.intersection(animals)); fruits.difference_update(animals)
print("Final set of 'fruits'",fruits)