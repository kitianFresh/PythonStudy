#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
def checkbmp(s):
	t = struct.unpack('<ccIIIIIIHH', s)
	print(type(t))
	if t[0] == b'B' and t[1] == b'M':
	    print('Yes! size: %d color: %d' % (t[2], t[9]))
	else:
		print('No!')
bmp_header = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
checkbmp(bmp_header)