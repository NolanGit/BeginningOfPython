#coding=utf-8
#生成器只在被调用的时候才计算数值，节省资源
g=(x*x for x in range(10))
print(g)
for n in g:
	print(n)
#斐波那契数列
#使用yield而不是print可以使他变成generator，遇到yield就中断，直到调用next或使用循环
def fib(max):
	n,a,b=0,0,1
	while n<max:
		yield(b)
		a,b=b,a+b#这两个是同时计算的，没有先后顺序
		n=n+1

fib(100)
g=fib(6)
while True:
	try:
		x=next(g)
		print('g:',x)
	except StopIteration as e:
		print('generator return value :',e)
		break
#杨辉三角
def triangles(x):
	L=[1]
	count =0
	while count<x:
		yield L
		L=[1]+[(L[i-1]+L[i]) for i in range(1,len(L))]+[1]
		count+=1
for n in triangles(10):
	print(n)