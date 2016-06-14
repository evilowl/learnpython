#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

test = '011-98907'
if re.match(r'^\d{3}\-\d{3,8}$', test):
	print 'ok'
else:
	print 'failed'

print 'a b    c'.split(" ")
print re.split(r'\s+', 'a  b bbb cc   ccc')
print re.split(r'[\s\,\;\|]+', 'a;d,d;d  ccc, |dfas')

#加入（）进行分组
m = re.match(r'^(\d{3})\-(\d{3,8})$', test)
print m.group(0)
print m.group(1)
print m.group(2)

print re.match(r'^(\d+)(0*)$', '10223000022000').groups()
print re.match(r'^(\d+?)(0*)$', '10223000022000').groups()

re_telephone = re.compile(r'^(\d{3})\-(\d{3,8})$')
print re_telephone.match('021-63939999').groups()

re_mail = re.compile(r'^([\d\w\.\_]+)@([\d\w]+)\.\w{3,8}$')
re_mail2 = re.compile(r'^(<[\w]+\s[\w]+>)\s([\d\w\.\_]+)@([\d\w]+)\.\w{3,8}$')

mail1 = 'someone@gmail.com'
mail2 = 'bill.gates@microsoft.com'
mail3 = '<Tom Paris> tom@voyager.org'

if re_mail.match(mail1):
	print 'ok'
if re_mail.match(mail2):
	print 'ok'
if re_mail2.match(mail3):
	print 'ok'
print re_mail2.match(mail3).groups()