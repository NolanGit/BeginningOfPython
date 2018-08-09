# coding=utf-8

try:
    print('try...')
    a = 10 / 0
    print('result:', a)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
print('-------------------')
try:
    print('try...')
    a = 10 / int(9)
    print('result:', a)
except ZeroDivisionError as z:
    print('ZeroDivisionError', z)
except ValueError as v:
    print('ValueError', v)
else:  # 要所有的except都写完之后才可以加上else
    print('No Error')
finally:
    print('finally...')
print('END')
print('-------------------')
# 互相调用的也可以捕获深层的异常


def first(a):
    return 10 / a


def second(b):
    return first(b)


def main():
    try:
        print(second('0'))
    except Exception as e:
        print('Error', e)
    finally:
        print('finally...')
main()
# logging模块可以打印错误信息后使程序继续执行
import logging


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
print('-------------------')
# 错误是cclass，捕获到一个错误就是捕获到该class的一个实例
'''
class FooError(ValueError):
	pass
def foo(s):
	n=int(s)
	if n==0:
		raise FooError('invalid value: %s' %s)
foo(0)
'''
# 运行下面的代码，根据异常信息进行分析，定位出错误源头，并修复：
'''
print (a)
from functools import reduce
def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
'''
print(a)
from functools import reduce


def str2num(s):
    try:
        return int(s)
    except ValueError as e:
        return float(s)


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()
