#!/usr/bin/python3
""" Utility to get system info """
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
import json


def get_ip_address():
    """ get ip address """
    proc = subprocess.run(
        ['ip', '-4', '-json', 'addr'], stdout=subprocess.PIPE)
    addr_json = json.loads(proc.stdout.decode("utf-8"))
    print('> IP Config:')
    for item in addr_json:
        for addr in item['addr_info']:
            print("IP address:", addr['local'])


def get_user_info():
    """ get user info """
    proc = subprocess.run('who', stdout=subprocess.PIPE)
    user = re.match(r'^(\S+)\s+(\S+)\s+([^\(]+)',
                    proc.stdout.decode("utf-8")).groups()
    print('> User info:')
    print("User name:", user[0])
    print("User terminal:", user[1])
    print("User session started at:", user[2])


def get_average_load():
    """ get average load """
    with open('/proc/loadavg') as ifile:
        avg = ifile.read()
    avg_data = re.match(r'^([\d.]+)\s+([\d.]+)\s+([\d.]+)', avg).groups()
    print('> System load average:')
    print("Load 1/5/15 min:", ' '.join(avg_data))


def get_cpu_info():
    """ get CPU info """
    with open('/proc/cpuinfo') as ifile:
        cpu = ifile.read()
    speed = re.findall(r"cpu MHz[\s:]+([\d]+)", cpu)
    regex = re.compile(r"(?P<name>(?:model name|cpu cores|siblings))[\s:]"
                       r"+(?P<val>.+)")
    cpu_data = {m.groupdict()['name']: m.groupdict()['val']
                for m in regex.finditer(cpu)}
    print('> CPU info:')
    print("CPU model:", cpu_data['model name'])
    print("Cores / Threads: {} / {}".format(cpu_data['cpu cores'],
                                            cpu_data['siblings']))
    print("Current thread speed (MHz):", " ".join(speed))


def get_memory_info():
    """ get memory info """
    with open('/proc/meminfo') as ifile:
        mem = ifile.read()
    regex = re.compile(r"(?P<name>(?:MemTotal|MemFree))[\D]+(?P<val>[\d]+)")
    mem_data = {m.groupdict()['name']: int(m.groupdict()['val'])
                for m in regex.finditer(mem)}
    print('> RAM memory stats:')
    print("Total:", mem_data['MemTotal'])
    print("Used: {}".format(mem_data['MemTotal'] - mem_data['MemFree']))
    print("Free:", mem_data['MemFree'])


def get_distro_info():
    """ get distributive info """
    with open('/etc/os-release') as ifile:
        os_data = ifile.read()
    os_version = re.search(r'PRETTY_NAME=\"(.*)\"', os_data)
    if os_version:
        print('> OS distro version:')
        print(os_version[1])
    else:
        print('> OS distro version: UNKNOWN')


def main():
    """ Main routine """
    parser = argparse.ArgumentParser(description='Show system information')
    parser.add_argument('-d', '--distro', action='store_true',
                        help='Get distro name')
    parser.add_argument('-m', '--memory', action='store_true',
                        help='Get info about RAM memory')
    parser.add_argument('-c', '--cpu', action='store_true',
                        help='Get info about CPU')
    parser.add_argument('-u', '--user', action='store_true',
                        help='Get info about user')
    parser.add_argument('-l', '--average', action='store_true',
                        help='Get info about load average')
    parser.add_argument('-i', '--ipaddress', action='store_true',
                        help='Get info about IP address')

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
        exit(1)

    if args.ipaddress:
        get_ip_address()

    if args.user:
        get_user_info()

    if args.average:
        get_average_load()

    if args.cpu:
        get_cpu_info()

    if args.memory:
        get_memory_info()

    if args.distro:
        get_distro_info()


if __name__ == "__main__":
    main()
