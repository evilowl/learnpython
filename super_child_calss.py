#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Animal(object):
	pass

class RunnableMixin(object):
	def run(self):
		print('Running...')

class FlyableMixin(object):
	"""docstring for Flyable"""
	def Fly(self):
		print('Flying')

#big class
class Mammal(Animal):
	pass

class Bird(Animal):
 	pass

# kind of Animal
class Dog(Mammal, RunnableMixin):
	pass

class Bat(Mammal, FlyableMixin):
	pass

class Parrot(Bird):
	"""docstring for Parrot"""
	pass

class Ostrich(Bird):
	pass


		