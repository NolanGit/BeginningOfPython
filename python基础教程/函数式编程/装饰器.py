#coding=utf-8 
#一个修饰符就是一个函数，它将被修饰的函数作为参数
#不传入参数的log()
import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args,**kw):#wrapper()函数内，首先打印日志，再紧接着调用原始函数
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now():
	print('2018.4.8')
now()

print('------------------')
#传入参数的log()
#首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
def log2 (text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print('%s,%s():'%(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator
@log2('execute')
def now2():
	print('2018.4.24')
now2()

print('-----------')
#请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time
def metric(fn):
	@functools.wraps(fn)
	def decorator(*args,**kw):
		start_time=time.time()
		fn(*args,**kw)
		print('%s executed in %s ms'%(fn.__name__,(time.time()-start_time)))
		return fn(*args,**kw)
	return decorator
@metric	
def testFn():
	a=1
	for x in range(1,100000):
		a=x*a
testFn()