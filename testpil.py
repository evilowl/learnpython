#!/usr/bin/env python
#-*-coding:utf-8 -*-

import Image
im = Image.open('test.jpg')
print im.format, im.size, im.mode

im.thumbnail((200, 300))
im.save('thumb.jpg', 'JPEG')

def readImage(fp):
	if hasattr(fp, 'read'):
		return readData(fp)
	return None