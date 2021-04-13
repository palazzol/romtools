#!/usr/bin/python

import sys

if len(sys.argv) <= 2:
    print('Usage: romjoin <newfilename> <filename1> <filename2> ...')
    sys.exit(0)

filename = sys.argv[1]
files = sys.argv[2:]

with open(filename,'wb') as f:
    for fname in files:
        with open(fname,'rb') as fin:
            fin.seek(0,2)
            size = fin.tell()
            fin.seek(0)
            data = fin.read()
            f.write(data)

