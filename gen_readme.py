#!/usr/bin/env python3

import os
import re

ROOT_DIR='.'

HEADER = """
# TIL

> Today I Learned

A collection of concise write-ups on small things I learn day to day.

## Items

"""
FOOTER = """

## About

I shamelessly stole this idea from
[jbranchaud/til](https://github.com/jbranchaud/til).

"""

print(HEADER)

prev_dir=None
for directory, dirs, files in os.walk(ROOT_DIR):
    # for i in range(len(dirs)):
    for dirname in list(dirs):
        if dirname.startswith(('.', '_')):
            dirs.remove(dirname)
    for filename in files:
        if directory == ROOT_DIR:
            continue
            
        title = re.sub(r'\.md$', '', filename).replace('-', ' ').title()
        base_dir = re.sub(r'^./', '', directory)
        
        if not directory == prev_dir:
            prev_dir=directory
            print("### {}".format(base_dir.title()))
            
        print("- [{}]({})".format(title, os.path.join(base_dir,filename)))
        
print(FOOTER)