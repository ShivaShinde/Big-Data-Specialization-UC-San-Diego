#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: MapReduce_Join2.py
Author: Shiva Shinde
Description: Mapper function.
"""
import sys

for line in sys.stdin:
    tv_show, value = line.split(',')
    tv_show = tv_show.strip()
    value = value.strip()

    if value.isdigit() or value == 'ABC':
        print('{0}\t{1}'.format(tv_show, value))