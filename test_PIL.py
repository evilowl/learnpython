#!/usr/bin/env python
#-*-coding:utf-8 -*-

import Image, ImageFilter

# 打开一个jpg图像文件
im = Image.open('test.jpg')

#获得图片尺寸
w, h = im.size

im.thumbnail((w//2, h//2))

im.save('test2.jpg', 'jpeg')


im2 = im.filter(ImageFilter.BLUR)
im2.save('test3.jpg', 'jpeg')