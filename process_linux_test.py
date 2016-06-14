import os

print 'process(%s) start...' % os.getpid()
pid = os.fork()
if pind == 0:
	print 'I am child process (%s) and my parents is %s' % (os.getpid(), os.getpid())
else:
	print 'I (%s) just created a child process(%s).' %(os.getpid(), pid)