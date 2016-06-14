#!/usr/bin/env python
#-*-coding: utf-8 -*-

import poplib
import email
from email.parser import Parser
from email.header import header
from email.utils import parseaddr

# indent used to suo display
def print_info(msg, indent = 0):
	if indent == 0:
		for header in ['Form', 'To', 'Subject']:
			value = msg.get(header, '')
			if value:
				if header == 'Subject':
					value = decode_str(value)
				else:
					hdr, addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s <%s>' %(name, addr)
			print '%s%s: %s' %('    ' * indent, header, value)

	if (msg.is_multipart()):
		# if email object is a MIMEMuitipart
		# get_payload() return list which concive all children objects
		parts = msg.get_payload()
		for n, part in enumerate(parts):
			print ('%s Part %s' % ('   ' * indent, n))
			print ('%s-------------------' % ('      ' * indent))
			print_info(part, indent + 1)
	else:
		# emial object isn't a MIMEMuitipart
		# accoding content_type judge
		content_type = msg.get_content_type()
		if content_type == 'text/plain' or content_type == 'text/html':
			content = msg.get_payload(decode = True)
			charset = guess_charset(msg)
			if charset:
				content = content.decode(charset)
			print ('%s Text: %s' % ('   ' * indent, content + "...."))
		else:
			# not a text, as deal
			print ('%s attachment: %s' % ('    ' * indent, content_type))

def decode_str(s):
	value, charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

def guess_charset(msg):
	# first get code from msg object
	charset = msg.get_charset()
	if charset is None:
		# if can't get , get it from content_type
		content_type = msg.get('Content-Type', '').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset




# input email address,password and poplib3 server address
email = raw_input('email:')
password = raw_input('password:')
pop3_server = raw_input('pop3 server:')

# connect pop3 server
server = poplib.POP3(pop3_server)
#open debuginfo
server.set_debuglevel(1)
print(server.getwelcome())
#idcard contonce
server.user(email)
server.pass_(password)
# stat() return email count and area
print ('messages: %s, Size: %s' server.stat())
# list() return all emails' id
resp, mails, octets = server.list()
print(mails)
# get the new email
index = len(mails)
resp, lines, octests = server.retr(index)
msg_content = '\r\n'.join(lines)
msg = Parser().parsester(meg_content)
# delete email from server according to email index
#server.dele(index)
# close connection
server.quit()
