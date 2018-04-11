#coding=utf-8
#实现X！
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
print fact(4)
#上边的实现方式会产生栈溢出问题，需要改为尾递归
def betterfact(n):
	return fact_iter(n,1)
def fact_iter(n,product):
	if n=1:
		return product
	return fact_iter(n-1,n*product)#在函数调用前就会被计算的参数就可以解决栈溢出问题了
