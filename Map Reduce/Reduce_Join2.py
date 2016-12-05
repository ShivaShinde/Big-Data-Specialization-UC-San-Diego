#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: Reduce_Join2.py
Author: Shiva Shinde
Description: Reducer function.
"""
import sys

prev = ""
flag = False
running_total = 0

for line in sys.stdin:
    line = line.strip()
    curr_tv_show, value = line.split('\t')

    if curr_tv_show != prev:
        if flag:
            print('{0} {1}'.format(prev, running_total))
        flag = False
        running_total = 0

    prev = curr_tv_show

    if value.isdigit():
        running_total += int(value)
    else:
        flag = True

if flag:
    print('{0} {1}'.format(prev, running_total))