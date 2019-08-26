#!/usr/bin/python3

# 6. Write a program that performs file backups (/etc/passwd, /etc/group, /etc/shadow).
# Add files to tar archive, name it as backup_{system_date_and_time}
# and put it to your home directory. Print out tar archives, which are located in your home folder.
# This should return last 10 archives. All other should be deleted. Use tar lib to create archive.


import tarfile
import sys
import datetime
import os
import re

backupDir = os.getenv("HOME")
backupList = ["/etc/passwd", "/etc/group", "/etc/shadow"]

date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
tarName = "%s/backup_%s.tar" % (backupDir, date)

tar = tarfile.open(tarName, "w")
for name in backupList:
    tar.add(name)
tar.close()

i = 0
for name in sorted(os.listdir(backupDir), reverse=True):
    if os.path.isfile(os.path.join(backupDir, name)):
        if re.match(r'backup_[\d]{8}_[\d]{6}.tar', name) != None:
            i += 1
            if i <= 10:
                print(name)
            else:
                os.remove(os.path.join(backupDir, name))
