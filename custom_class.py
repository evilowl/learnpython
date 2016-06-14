#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Student():
	def __init__(self, name):
		self.name = name
	def __str__(self):
		return "Student object (name: %s)" % self.name
	__repr__ = __str__

	def __getattr__(self, attr):
		if attr == 'score':
			return 99
		if attr == 'age':
			return lambda: 25
		raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

	def __call__(self):
		print ('my Name is %s. ' % self.name)


print Student("Michael")
s = Student('xiaoming')
s()

class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1

	def __iter__(self):
		return self

	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 10000:
			raise StopIteration();
		return self.a

	def __getitem__(self, n):
		if isinstance(n, int):
			a, b = 1, 1
			for x in range(n):
				a, b = b, a + b
			return a
		if isinstance(n, slice):
			start = n.start
			stop = n.stop
			a, b = 1, 1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a, b =  b, a + b
			return L

class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		return Chain('%s/%s' % (self._path, path))

	def __str__(self):
		return self._path

	__repr__ = __str__
		
# for n in Fib():
# 	print n

# print Fib()[5]
# print Fib()[1:8]
# s = Student('ddd')
# print s.score
# print s.age()
