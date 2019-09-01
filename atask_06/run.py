#!/usr/bin/python3
""" Backup files """
# 6. Write a program that performs file backups
# (/etc/passwd, /etc/group, /etc/shadow).
# Add files to tar archive, name it as backup_{system_date_and_time}
# and put it to your home directory. Print out tar archives,
# which are located in your home folder.
# This should return last 10 archives. All other should be deleted.
# Use tar lib to create archive.


import tarfile
import sys
import datetime
import os
import re
import argparse


def init_vars():
    """ Parse args and prepare variables """
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--destination', default=os.getenv("HOME"),
                        help='Path to directory with backups.')
    parser.add_argument('-f', '--file', nargs='?', action='append',
                        help='Which file to backup. Flag can be '
                             'used multiple times to backup many files.')
    args = parser.parse_args()

    if args.file:
        tmp_backup_list = args.file
    else:
        tmp_backup_list = ["/etc/passwd", "/etc/group", "/etc/shadow"]

    backup_list = []
    for item in tmp_backup_list:
        if not os.path.isfile(item):
            print(f"Got item '{item}', that is not file. Exit.")
            sys.exit(1)
        if not os.access(item, os.R_OK):
            print(f"Can not access file '{item}'. Exit.")
            sys.exit(1)
        backup_list.append(item)

    if args.destination:
        backup_dir = args.destination
        if not os.path.isdir(backup_dir):
            print(f"Destination path '{backup_dir}' is not valid directory. "
                  "Exit.")
            sys.exit(1)
        if not os.access(backup_dir, os.R_OK):
            print(f"Can not access destination directory '{backup_dir}'. "
                  "Exit.")
            sys.exit(1)

    return backup_list, backup_dir


def main(backup_list, backup_dir):
    """ Main routine """

    date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    tar_name = f"{backup_dir}/backup_{date}.tar"

    try:
        tar = tarfile.open(tar_name, "w")
        for name in backup_list:
            tar.add(name)
        tar.close()
    except OSError as err:
        print("Error with file handling.", err)
        sys.exit(1)

    i = 0
    for name in sorted(os.listdir(backup_dir), reverse=True):
        if os.path.isfile(os.path.join(backup_dir, name)):
            if re.match(r'backup_[\d]{8}_[\d]{6}.tar', name):
                i += 1
                if i <= 10:
                    print(name)
                else:
                    os.remove(os.path.join(backup_dir, name))


if __name__ == "__main__":
    BFILES, BDIR = init_vars()
    main(BFILES, BDIR)
