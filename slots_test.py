#!/usr/bin/env python
#-*- coding: utf-8 -*-

from types import MethodType

class  Student(object):
	"""docstring for  Student"""
	pass

def set_age(self, age):
	self.age = age

s = Student()
s2 = Student()
s.set_age = MethodType(set_age, s, Student)
s.set_age(25)
print s.age

def set_score(self, score):
	self.score = score
Student.set_score = MethodType(set_score, None, Student)

s.set_score(20)
print s.score
s2.set_score(100)
print s2.score

class Worker(object):
	__slots__ = ('name', 'age')

w = Worker()
w.name = 'jjj'
w.age = 100

class Programer(Worker):
	pass
p = Programer()
p.money = 1000