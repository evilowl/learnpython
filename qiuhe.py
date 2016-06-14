def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print 'name', name, 'age', 'other',kw

def func(a, b, c=0, *args, **kw):
    print 'a=', a, 'b=',b, 'c=', c, 'args=', args, 'kw=', kw
    
    

def fact(n):
    if n == 1:
        return 1
    # print n
    return n * fact(n - 1)

def facts(n):
    return facts_iter(n, 1)
def facts_iter(num, product):
    if num == 1:
        return product
    return facts_iter(num - 1, num * product)

def fib(max):
    n , a, b = 0, 0, 1
    while n < max:
        #print b
        yield b
        a, b = b, a + b
        n = n + 1

def f(x):
    return x * x
def fn(x, y):
    return x * 10 + y

def srt2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}[s]
    return reduce(fn, map(char2num, s))

        
