#!/usr/bin/python

import sys

if len(sys.argv) != 3:
    print('Usage: romsplit <filename> <numfiles>')
    sys.exit(0)

filename = sys.argv[1]
num_files = int(sys.argv[2])
x = filename.split('.')
if len(x) > 1:
    suffix = '.'+x[-1]
    x.pop()
    prefix = '.'.join(x)
else:
    prefix = x[0]
    suffix = ''

with open(filename,'rb') as f:
    f.seek(0,2)
    size = f.tell()
    f.seek(0)
    if size % num_files != 0:
        print('Error: File size not divisible by number of files')
        sys.exit(0)
    small = size // num_files
    for i in range(0,num_files):
        data = f.read(small)
        with open(prefix+'_'+str(i)+suffix,'wb') as fout:
            fout.write(data)
