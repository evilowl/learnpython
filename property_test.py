#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class Student(object):
# 	'''about a Student data'''
# 	def get_score(self):
# 		return self.__score

# 	def set_score(self, value):
# 		if not isinstance(value, int):
# 			raise ValueError('score must be integer!')
# 		if value < 0 or value > 100:
# 			raise ValueError('score must between 0~100!')
# 		self.__score = value

# s = Student()
# s.set_score(80)
# print s.get_score()
# s.set_score(10000)


class Student(object):
	''' discrabe Student'''

	@property
	def score(self):
		return self.__score

	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be integer')
		if value < 0 or value > 100:
			raise ValueError('score must between 0~100')
		self.__score = value


s = Student()
s.score = 80
print s.score

class teacher(object):
	"""docstring for teacher"""
	
	@property
	def birth(self):
		return self.__birth

	@birth.setter
	def birth(self, value):
		self.__birth = value

	@property
	def age(self):
		return 2016 - self.__birth
		