#!/usr/bin/python3
""" User Agent statistic from given access.log file """
# 6. Create script which reads access log from file
# (name of file is provided as argument).
# As output script should provide total number of different User Agents
# and than provide statistic with number of requests from each of them.

import sys
import re
import os


def main():
    """ Main routine User Agent"""
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} FILE\nExit.")
        sys.exit(1)

    if not os.access(sys.argv[1], os.R_OK) and not os.path.isfile(sys.argv[1]):
        print("Typed JSON file not found or no permissions to access. Exit.")
        sys.exit(1)

    used = {}
    with open(sys.argv[1]) as read_file:
        regex = r"[\d\.]+ . . .+ .+ [\d]+ [\d]+ .+ (\".+\")"
        for line in read_file:
            u_a = re.findall(regex, line)[0]
            ha_ua = str(hash(u_a))
            if ha_ua in used:
                used[ha_ua]['count'] += 1
            else:
                used[ha_ua] = {}
                used[ha_ua]['ua'] = u_a
                used[ha_ua]['count'] = 1

    used_sort = dict(sorted(used.items(), key=lambda x: x[1]['count'],
                            reverse=True))

    print("Total number of different User Agents:", len(used_sort))
    print("User Agents usage statistic:")
    for item in used_sort.values():
        print(item['count'], "times used ", item['ua'])


if __name__ == "__main__":
    main()
