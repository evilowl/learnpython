#!/usr/bin/env python
#-*-coding: utf-8 -*-

import hashlib

md5 = hashlib.md5()
md5_2 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
md5_2.update('how to use md5')
md5_2.update('i python hashlib?')
print md5.hexdigest()
print md5_2.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use sha1 in ')
sha1.update('python hashlib?')
print sha1.hexdigest()


db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def cald_md5(password):
	md5 = hashlib.md5()
	md5.update(password)
	return md5.hexdigest()

def login(user, password):
	if db[user] == cald_md5(password):
		return True
	else:
		return False

print login('bob', '888888')