#!/usr/bin/env python
#-*- coding: utf-8 -*-

# def foo():
# 	r = some_function()
# 	if r == (-1):
# 		return (-1)
# 	#do something
# 	return r

# def bar():
# 	r = foo()
# 	if r == (-1):
# 		print "error"
# 	else:
# 		pass

try:
	print 'try ...'
	r = 10 / 5
	print 'result:', r
except ZeroDivisionError, e:
	print 'except:', e
finally:
	print 'finally...'
print 'END'

try:
	print 'try...'
	r = 10 / int('1')
	print 'result:', r
except ValueError, e:
	print 'ValueError:', e
except ZeroDivisionError, e:
	print 'ZeroDivisionError:', e
else:
	print 'no error!'
finally:
	print 'finally...'
print 'END'

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except StandardError, e:
		print 'error'
	else:
		pass
	finally:
		print 'finally...'

main()