#!/usr/bin/python3

# 13. Remove duplicate from a list and create a tuple and find the minimum and maximum number.

nums = [1, 8, 2, 3, 4, 5, 5, 4, 3, 2, 1, 6]
print("Defined list: ", nums)

uniq_nums = []
for num in nums:
    if num not in uniq_nums:
        uniq_nums.append(num)
print("Same list without duplicates:", uniq_nums)

tupl = (min(uniq_nums), max(uniq_nums))
print("Tuple with min and max:", tupl)
