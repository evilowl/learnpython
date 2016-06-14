#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Hello(object):
	"""docstring for Hello"""
	def hello(self, name = 'world'):
		print 'Hello, %s' %name

def fn(self, name = 'world'):
	print 'Hello, %s' % name

Hi = type('Hi', (object,), dict(hi=fn))

h = Hi()
h.hi()
print type(h)
print type(Hi)

#测试元类
class ListMetaclass(type):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)

class myList(list):
	"""docstring for List"""
	__metaclass__ = ListMetaclass
		
l = myList()
l.add(1)
print l
