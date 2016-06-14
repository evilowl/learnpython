def prod(s):
    def calc(a, b):
        return a*b
    print reduce(calc, s)

def normalize(s):
    #return s.title()   #title() string 中的内建函数
    return s[0].upper() + s[1:].lower() #大写，小写函数

print map(normalize, ['djkkKK', 'd', 'kkkLLL', 'KKK'])

def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x,y: x*10 + y, map(char2num,s))
def is_odd(n):
	return n % 2 == 1
filter(is_odd, [1,2,3,4,5,6,7,8,9,0])

def not_empty(s):
	return a and s.stip()
import math
#打印所有的非质数
def not_su(s):
	if s==1:
		return 1
#	if s==2:
#		return 0
	k = int(math.sqrt(s))
	for i in range(2,k+1):
		if (s%i == 0):
			return 1
	return 0
print filter(not_su, range(1, 101))
#打印所有的质数
def isPermise(s):
	if s == 1:
		return 0
	for i in range(2, s):
		if(s%i == 0):
			return 0
	return 1
print filter(isPermise, range(1, 101))