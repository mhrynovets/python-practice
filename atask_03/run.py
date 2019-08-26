#!/usr/bin/python3

# 3. Write script which gets system information like
# distro info,
# memory(total, used, free),
# CPU info (model, core numbers, speed),
# current user,
# system load average,
# IP address.
# Use params for specifying resource. (e.g.
# -d for distro
# -m for memory,
# -c for CPU,
# -u for user info,
# -l for load average,
# -i for IP address).
# Use subprocess module and read files from /proc directory.
# You can use argparse lib for argument parsing.import sys

import argparse
import re
import subprocess

parser = argparse.ArgumentParser(description='Show system information')
parser.add_argument('-d', '--distro', action='store_true', help='Get distro name')
parser.add_argument('-m', '--memory', action='store_true', help='Get info about RAM memory')
parser.add_argument('-c', '--cpu', action='store_true', help='Get info about CPU')
parser.add_argument('-u', '--user', action='store_true', help='Get info about user')
parser.add_argument('-l', '--average', action='store_true', help='Get info about load average')
parser.add_argument('-i', '--ipaddress', action='store_true', help='Get info about IP address')

args = parser.parse_args()
if not any(vars(args).values()):
    parser.print_help()
    exit(1)


if args.ipaddress:
    proc = subprocess.run(['ip', 'route', 'get', '8.8.8.8'], stdout=subprocess.PIPE)
    addr = re.search(r'src ([\d\.]+)', proc.stdout.decode("utf-8")).groups()
    print()
    print('> IP Config:')
    print("IP address:", addr[0])


if args.user:
    proc = subprocess.run('who', stdout=subprocess.PIPE)
    user = re.match(r'^(\S+)\s+(\S+)\s+([^\(]+)', proc.stdout.decode("utf-8")).groups()
    print()
    print('> User info:')
    print("User name:", user[0])
    print("User terminal:", user[1])
    print("User session started at:", user[2])


if args.average:
    with open('/proc/loadavg') as f:
        avg = f.read()
    avgData = re.match(r'^([\d.]+)\s+([\d.]+)\s+([\d.]+)', avg).groups()
    print()
    print('> System load average:')
    print("Load 1/5/15 min:", ' '.join(avgData))


if args.cpu:
    with open('/proc/cpuinfo') as f:
        cpu = f.read()
    speed = re.findall(r"cpu MHz[\s:]+([\d]+)",cpu)
    r = re.compile(r"(?P<name>(?:model name|cpu cores|siblings))[\s:]+(?P<val>.+)")
    cpuData = { m.groupdict()['name']:m.groupdict()['val'] for m in r.finditer(cpu) }
    print()
    print('> CPU info:')
    print("CPU model: %s" % (cpuData['model name']))
    print("Cores / Threads: %s / %s" % (cpuData['cpu cores'], cpuData['siblings']))
    print("Current thread speed (MHz):", " ".join(speed))


if args.memory:
    with open('/proc/meminfo') as f:
        mem = f.read()
    r = re.compile(r"(?P<name>(?:MemTotal|MemFree))[\D]+(?P<val>[\d]+)")
    memData = { m.groupdict()['name']:int(m.groupdict()['val']) for m in r.finditer(mem) }
    print()
    print('> RAM memory stats:')
    print("Total: %s" % memData['MemTotal'])
    print("Used: %s" % (memData['MemTotal'] - memData['MemFree']))
    print("Free: %s" % memData['MemFree'])


if args.distro:
    with open('/etc/issue') as f:
        osVersion = f.read()
    print()
    print('> OS distro version:')
    print(osVersion[0:-8:])
