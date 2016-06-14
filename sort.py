#!/usr/bin/env python
def reversed_cmp(x, y):
	if x > y:
	    return -1
	if x < y:
	    return 1
	return 0

def cmp_ignore_case(s1, s2):
	##u1 = s1.upper()
	##u2 = s2.upper()
	u1 = s1.title()
	u2 = s2.title()
	if u1 < u2:
		return - 1
	if u1 > u2:
		return 1
	return 0

def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = n + ax
		return ax
	return sum

def count():
	fs = []
	for i in range(1, 4):
		def f(j):
			def g():
				return j * j
			return g
		fs.append(f(i))
	return fs
f1, f2, f3 = [(lambda i = j : i ** 2) for j in range(1,4)]

##def log(func):
##	def wrapper(*args, **kw):
##		print 'call %s():' % func.__name__
##		return func(*args, **kw)
##	return wrapper
##def log(text):
##    def decorator(func):
##        def wrapper(*args, **kw):
##            print '%s %s():' %(text, func.__name__)
##            return func(*args, **kw)
##
##        return wrapper
##    return decorator
##@log('execute')
import functools

'''def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
    '''
def log(func):
	@functools.wraps(func)
	def  wrapper(*args, **kw):
		print 'begin call'
		func(*args, **kw)
		print 'end call'
	return wrapper


@log
def now(s):
	print '2014.369 is %s' %s
	
now('aa')
