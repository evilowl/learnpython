#!/usr/bin/env python
# -*- coding:utf-8 -*-

import base64

bstring = base64.b64encode('just coding\x00string')
print bstring
destring = base64.b64decode(bstring)
print destring

print base64.b64encode('binary\x00string')
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
#print base64.urlsafe_b64decode('abcd--__')

def safe_b64decode(str):
	return base64.b64decode(str+(4-(len(str)%4))*'=')

print safe_b64decode('YWJjZA')