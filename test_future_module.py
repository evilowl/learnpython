#!/usr/bin/env python
#-*-coding:utf-8 -*-

# still running on python 2.7.11

from __future__ import unicode_literals,division

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\'is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\'  is str?', isinstance('xxx', str)
print 'b\'xxx\' is str', isinstance(b'xxx', str)


print '10 / 3 = ', 10 / 3 
print '10.0 / 3 = ', 10.0 / 3 
print '10 // 3 = ', 10 // 3