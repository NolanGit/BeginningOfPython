#coding=utf-8 
import functools
int2=functools.partial(int,base=2)#总结functools.partial的作用就是，把一个函数的某些参数给固定住
print(int2('100000'))
print(int2('100000',base=10))