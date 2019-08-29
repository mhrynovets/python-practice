#!/usr/bin/python3

# 13. Remove duplicate from a list 
# and create a tuple and find the minimum and maximum number.
import sys

if len(sys.argv) != 2:
    print("Usage: %s FILE" % sys.argv[0])
    print("Exit.")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        line = f.readline()
        nums = [int(x.strip()) for x in line.split(",") if x.strip() != ""]
except OSError as err:
    print("OS error: {0}".format(err))
    sys.exit(1)
except ValueError:
    print("Some values in file are not numbers.")
    print([x.strip() for x in line.split(",") if x.strip() != ""])
    sys.exit(1)
except:
    print("Unexpected error:", sys.exc_info()[0])
    sys.exit(1)

print("Defined list: ", nums)

uniq_nums = []
for num in nums:
    if num not in uniq_nums:
        uniq_nums.append(num)
print("Same list without duplicates:", uniq_nums)

tupl = (min(uniq_nums), max(uniq_nums))
print("Tuple with min and max:", tupl)
