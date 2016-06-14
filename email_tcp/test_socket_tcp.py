#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import socket

#创建一个连接
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
sk.connect(('www.163.com', 80))
# send request
sk.send('GET / HTTP/1.1\r\n Host: www.163.com \r\nConnection: close\r\n\r\n')

buffer1 = []
#接受数据
while True:
	d = sk.recv(1024)
	if d :
		buffer1.append(d)
	else:
		break

data = ''.join(buffer1)
sk.close()
header, html = data.split('\r\n\r\n', 1)
print header
#print data
#接收的数据写入文件
with open('baidu.html', 'wb') as fl:
	fl.write(html)
