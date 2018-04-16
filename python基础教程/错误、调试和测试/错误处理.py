#coding=utf-8

try:
	print('try...')
	a=10/0
	print('result:',a)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')
print('-------------------')
try:
	print('try...')
	a=10/int(2)
	print('result:',a)
except ZeroDivisionError as z:
	print('ZeroDivisionError',z)
except ValueError as v:
	print('ValueError',v)
else:#要所有的except都写完之后才可以加上else
	print('No Error')
finally:
	print('finally...')
print('END')
print('-------------------')
#互相调用的也可以捕获深层的异常
def first(a):
	return 10/a
def second(b):
	return first(b)
def main():
	try:
		print(second('0'))
	except Exception as e:
		print('Error',e)
	finally:
		print('finally...')
main()
