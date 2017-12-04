#!/usr/bin/env python
# encoding=utf-8

import os, datetime

print('')

basedir = str(input("Please input the dir:"))

if os.path.isfile(basedir):
    lines = len(open(basedir, 'rU').readlines())
    print(basedir+str(lines)+'\n')
    os._exit(0)

if not os.path.isdir(basedir):
    print(basedir+'is not a directory\n')
    os._exit(1)

list = os.listdir(basedir)

total_lines = 0
file_list = {}
dirlist = [ basedir]

i = 0
# 遍历所有文件夹
while i < len(dirlist):
    basedir = dirlist[i]
    list = os.listdir(basedir)
    for j in range(0,len(list)):
        path = os.path.join(basedir, list[j])
        if os.path.isfile(path) and not path.endswith('~'):
            lines = len(open(path, 'rU').readlines())
            filelist[path] = lines
            total_lines += lines
        elif os.path.isdir(path):
            dirlist.append(path)

    i = i + 1
