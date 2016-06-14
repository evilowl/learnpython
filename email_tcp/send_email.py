#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((\
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))



#input email address and password

from_addr = ' @163.com'#raw_input('From:')
password = raw_input('password:')

# input smtp server address
smtp_server = 'smtp.163.com'#raw_input('smtp server:')
#input accept
to_addr = ' @163.com'#raw_input('to:')

# email zhen wen 
#msg = MIMEText('hello, send by python..', 'plain', 'utf-8')
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')  #发送html格式
msg = MIMEMultipart()
msg['From'] = _format_addr(u'python爱好者<%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自smtp的问候……', 'utf-8').encode()

#邮件正文
#msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
msg.attach(MIMEText('<html><body><h1>Hello</h1>' +
    '<p><img src="cid:0"></p>' +
    '</body></html>', 'html', 'utf-8'))

#添加邮件附件就是加上一个mimebase， 从本地读取一个图片
with open('thumb.jpg', 'rb') as f:
	#设置附件的mime和文件名， 这里是jpeg格式
	mime = MIMEBase('image', 'jpeg', filename = 'thumb.jpg')
	#加上头信息
	mime.add_header('Content-Disposition', 'attachment', filename='thumb.jpg')
	mime.add_header('Content-ID', '<0>')
	mime.add_header('X-Attachment-Id', '0')
	#把邮件内容读进来：
	mime.set_payload(f.read())
	#用base64编码
	encoders.encode_base64(mime)
	#添加到MIMEMulitipart
	msg.attach(mime)
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()