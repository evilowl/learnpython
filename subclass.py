#!/usr/bin/env python
# -*- coding:utf-8 -*-

import types

class Animal(object):
	def run(self):
		print 'Animal is running...'

class Dog(Animal):
	"""docstring for Dog"""
	def run(self):
		print 'Dog is running...'

	def eat(self):
		print 'Eating meat...'

class Cat(Animal):
	"""docstring for Cat"""
	def run(self):
		print 'Cat is running...'

class Tortoise(Animal):
	"""docstring for Tortoise"""
	def run(self):
		print 'Tortoise is running slowly...'
		

def runtwice(animal):
	animal.run()
	animal.run()
		
dog = Dog()
dog.run()
cat = Cat()
cat.run()

a = list()
b = Animal()
c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)
print isinstance(c, Animal)
print isinstance(b, Dog)

runtwice(Animal())
runtwice(Dog())
runtwice(Cat())
runtwice(Tortoise())

print type(123)
print type('123')
print type(None)
print type(True)
print type(abs)
print type(b)
print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
print type(str) == types.TypeType

print dir('123')