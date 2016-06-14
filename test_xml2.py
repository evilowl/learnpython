#!/usr/bin/env python
#-*-coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
import urllib

class DefaultSaxHandle(object):
	"""docstring for DefaultSaxHandle"""
	# def __init__(self):
	# 	self.key = {'city': None, 'pm25': None, 'time': None}

	# def start_element(self, name, attrs):
	# 	if name == 'city':
	# 		self.key['city'] = True
	# 	elif name == 'pm25':
	# 		self.key['pm25'] = True
	# 	elif name == 'time':
	# 		self.key['time'] = True

	# def char_data(self, text):
	# 	if self.key['city']:
	# 		print "city: %s" % text
	# 		self.key[city] = None
	# 	elif self.key['pm25']:
	# 		print 'pm25: %s' % text
	# 	elif self.key['time']:
	# 		print 'time；%s' % text
	def start_element(self, name, attrs):
		print "sax:start_element: %s, attrs: %s" %(name, str(attrs))
	
	def end_element(self, name):
		print 'sax:end_element: %s' % name

	def char_data(self, text):
		print 'sex:char_data: %s' % text


xml = urllib.urlopen('http://wthrcdn.etouch.cn/WeatherApi?citykey=101010100').read()
handler = DefaultSaxHandle()
parser = ParserCreate()
parser.returns_unicode = True
parser.StartElementHandler = handler.start_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)
