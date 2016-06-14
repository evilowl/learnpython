#!/usr/bin/env python
#-*-coding:utf-8 -*-

# try:
# 	f = open('../hello.py', 'r')
# 	print f.read()
# except IOError, e:
#   pass
# finally:
# 	if f:
# 		f.close()
with open('../hello.py', 'r') as f:
	#print f.read()
	for line in f.readlines():
		print (line.strip())

# with open('test.jpg', 'rb') as rf:
# 	print rf.read()

# with open('gbk.txt', 'rb') as f:
# 	u = f.read().decode('gbk')
# 	print u

# import codecs
# with codecs.open('gbk.txt', 'r', 'gbk') as f:
# 	print f.read()
	

with open('gbk.txt', 'w') as f:
        f.write('test')

import os

abspath = os.path.abspath('.')
print abspath
newpath = os.path.join(abspath, 'testdir')
print newpath
#os.mkdir(newpath) 
#os.rmdir(newpath)

filename = os.path.split('d:/work/python/liaoxuetest/gbk.txt')
print filename
extendname = os.path.splitext('d:/work/python/liaoxuetest/gbk.txt')
print extendname

dirx = [x for x in os.listdir('.') if os.path.isdir(x)]
print dirx
filex = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print filex