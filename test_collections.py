#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter


Point  = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print p.x, p.y
print isinstance(p, Point)
print isinstance(p, tuple)

Circle = namedtuple('Circle', ['x', 'y', 'r'])
circle1 = Circle(1, 2, 3)
print circle1.x,  circle1.y, circle1.r

#测试deque快速操作的双向链表
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print q

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print dd['key1']
print dd['key2']

d = dict([('a', 1), ('b', 2), ('c', 3)])
print d

od = OrderedDict([('a',1), ('b', 2), ('c', 3)])
print od 

od1 = OrderedDict()
od1['z'] = 1
od1['t'] = 2
od1['x'] = 9

print od1
print od1.keys()

class LastUpdateOrderedDict(OrderedDict):

	def __init__(self, capacity):
		super(LastUpdateOrderedDict, self).__init__()
		self._capacity = capacity

	def __setitem__(self, key , value):
		containsKey = 1 if key in self else 0
		if len(self) - containsKey >= self._capacity:
			last = self.popitem(last=False)
			'''last的关键字参数是OrderedDict.popitem()特有的，dict.popitem()没有这个参数,

				last=False就会按FIFO来删除对,即删除第一个key，如果last=True就会按LIFO来删除对，即删除最后一个key。

			'''
			print 'remove:', last
		if containsKey:
			del self[key]
			print 'set:', (key, value)
		else:
			print 'add:', (key, value)
		OrderedDict.__setitem__(self, key, value)

c = Counter() #字符计数器

for ch in 'programing and coding':
	c[ch] = c[ch] + 1

print c