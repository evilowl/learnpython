#!/usr/bin/env python
#-*-coding:utf-8 -*-

import socket,threading,time

def tcplink(sock, addr):
	print 'Accept new connection from %s:%s...' % addr
	sock.send('welcome!')
	while True:
		data  = sock.recv(1024)
		time.sleep(1)
		if data == 'exit' or not data:
			break
		sock.send('Hello, %s!' % data)
	sock.close()
	print 'connecting from %s:%s closed.' % addr


st = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#设置监听端口
st.bind(('127.0.0.1', 9999))
st.listen(5)
print 'wating for connecting'

while True:
	#接受一个新连接
	sock, addr = st.accept()
	#创建新线程来处理tcp连接
	t = threading.Thread(target = tcplink, args=(sock, addr))
	t.start()

