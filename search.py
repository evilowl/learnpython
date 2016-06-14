#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def search(keyword, path='.'):
	
	filenames = [x for x in os.listdir(path)]
	for file in filenames:
		abspath = os.path.abspath(path)+'/'+file
		if os.path.isdir(abspath):
			search(keyword, abspath)
		else:
			if keyword in file:
				print abspath

args = sys.argv
if len(args) == 2:
	search(args[1])
else:
	print 'Use : search.py arg'
	sys.exit()
