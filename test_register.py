#!/usr/bin/env python
#-*- coding:utf-8 -*-

import hashlib

db = {}

def get_md5(str):
	md5 = hashlib.md5()
	md5.update(str)
	return md5.hexdigest()

def register(usename, password):
	db[usename] = get_md5(password + usename + 'the-salt')

def login(usename, password):
	if db[usename] == get_md5(password + usename + 'the-salt'):
		return True
	else:
		return False


register('bob', '123456')
register('ming', '111')
print login('bob', '123')
print login('bob', '123456')