#coding=utf-8 
print(map(lambda x:x*x,[1,2,3,4,5]))
#lambda就是匿名函数,关键字lambda表示匿名函数，冒号前面的x表示函数参数。
f=lambda x:x*2
print(f)
def build(x,y):
	return lambda:x*x+y*y
'''
请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))
'''
print((filter(lambda x:x%2==1,range(1,20))))
