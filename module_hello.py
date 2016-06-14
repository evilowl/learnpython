#!/usr/bin/env python  
# -*-coding: utf-8 -*-
'a test module'

__auther__='miss tao'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print 'hello, world!'
	elif len(args) == 2:
		print 'Hello, %s!' % args[1]
	else:
		print 'Too many arguments!'

if __name__ == '__main__':
	test()

try:
	import cStringIO as StringIO
except ImportError: #fail 导入
    import StringIO