#!/usr/bin/env python
#-*-coding: utf-8 -*-

import itertools

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
for n in ns:
	print n

for c in itertools.chain('ABC', 'DEF'):
	print c

for key, group in itertools.groupby('AAABBBCCCAAA'):
	print key, list(group)

for key ,group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
	print key, list(group)