#coding=utf-8
#断言assert
'''
def foo(n):
	n=int(n)
	assert n!=0,"n is zero"#n不等于0应该为True，当assert为False的情况下抛出AssertionError
	return 10/n
foo(0)
'''
#可以使用 -0 参数来关闭assert，关闭后所有的Assert语句都相当于pass
import logging
logging.basicConfig(level=logging.INFO)#配置信息，可以记录记录信息的级别
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
print('End')
