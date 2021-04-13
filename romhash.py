#!/usr/bin/python

import sys
import binascii
import hashlib

if len(sys.argv) != 2:
    print('Usage: romhash <filename>')
    sys.exit(0)

filename = sys.argv[1]

with open(filename,'rb') as f:
    f.seek(0,2)
    size = f.tell()
    f.seek(0)
    contents = f.read(size)
    
checksum = 0
for i in range(0,size):
    checksum += contents[i]
checksum = checksum % 0x10000

sha1 = hashlib.sha1()
sha1.update(contents)
sha1hex = sha1.hexdigest()

crc32 = binascii.crc32(contents)

print('16-bit Checksum: {:02x}'.format(checksum))
print('          CRC32: {:08x}'.format(crc32))
print('           SHA1:',sha1.hexdigest())

