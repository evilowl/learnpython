#!/usr/bin/env python
#-*- coding:utf-8 -*-

class MyObject(object):
	"""docstring for MyObject"""
	def __len__(self):
		return 100
	def __init__(self):
		self.x = 10
	def power(self):
		return self.x * self.x

obj = MyObject()
print len(obj)
print hasattr(obj, 'x')
print obj.x
print hasattr(obj, 'y')
setattr(obj, 'y', 12)
print hasattr(obj, 'y')
print obj.y
print getattr(obj, 'y')
print getattr(obj, 'zz', 404)
print hasattr(obj, 'power')
print getattr(obj, 'power')
fn = getattr(obj, 'power')
print fn()