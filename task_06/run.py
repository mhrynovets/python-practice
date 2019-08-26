#!/usr/bin/python3

# 6. Create script which reads access log from file (name of file is provided as argument).
# As output script should provide total number of different User Agents
# and than provide statistic with number of requests from each of them.

import sys
import re


if (len(sys.argv) != 2):
    print("You should type a filename as argument!")
    sys.exit(1)

used = {}

with open(sys.argv[1]) as f:
    for line in f:
        ua = re.findall(r"[\d\.]+ . . .+ .+ [\d]+ [\d]+ .+ (\".+\")", line)[0]
        ha_ua = str(hash(ua))
        if ha_ua in used:
            used[ha_ua]['count'] += 1
        else:
            used[ha_ua] = {}
            used[ha_ua]['ua'] = ua
            used[ha_ua]['count'] = 1

used_sort = dict(sorted(used.items(), key=lambda x: x[1]['count'], reverse=True))

print("Total number of different User Agents:", len(used_sort))
print("User Agents usage statistic:")
for item in used_sort.values():
    print(item['count'], "times used ", item['ua'])
