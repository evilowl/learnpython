#!/usr/bin/env python
# -*- coding:utf-8 -*-

import struct

struct.pack('>I', 10240099)

def checkbmp(bmp_file):
	with open(bmp_file, 'rb')  as f:
		header = f.read(30)
		return checkbmp_header(header)

def checkbmp_header(header_in_byte):
	if len(header_in_byte) != struct.calcsize('>ccIIIIIIHH'):
		raise Exception('Invalid byte length: %Dn, except 30') %len(header_in_byte)
	info = struct.unpack(">ccIIIIIIHH", header_in_byte)
	if info[0] + info[1] in ('BM', 'BA'):
		from collections import namedtuple
		BMP_info = namedtuple("BMP_info", ['width', 'height'], ['color'])
		return BMP_info(info[6], info[7], info[9])
	else:
		return -1

path = "test.jpg"
checkbmp(path)