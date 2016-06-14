#!/usr/bin/env python
# -*- coding:utf-8 -*-

try:
	import cPickle as pickle
except ImportError:
	import pickle

import json

d = dict(name='bob', age=20, score=88)
print pickle.dumps(d)
json.dumps(d)

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

s = Student('bob', 20,  88)
print (json.dumps(s, default=lambda obj: obj.__dict__))

def student2dict(std):
	return {
		'name': std.name,
		'age': std.age,
		'score': std.score
	}

json_str = (json.dumps(s, default=student2dict))

def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

print(json.loads(json_str, object_hook=dict2student))