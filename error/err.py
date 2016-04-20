#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

# def foo(s):
# 	return 10 / int(s)

class FooError(StandardError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invalid value: %s' % s)
	return 10 / n

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except StandardError, e:
		logging.exception(e)

main()
print 'END'

