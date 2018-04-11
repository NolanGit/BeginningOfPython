#coding=utf-8 
def log(func):
	def wrapper(*args,**kw):#wrapper()函数内，首先打印日志，再紧接着调用原始函数
		print('call %s():'%func.__name__)
		return func(*args,**kw)
	return wrapper
#传入参数的log()
def log (text):
	def decorator(func):
		def wrapper(*args,**kw):
			print('%s,%s():'(text,func.__name__))
			return func(*args,**kw)
		return wrapper
	return decorator

@log
def now():
	print('2018.4.8')
now()
