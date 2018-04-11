#coding=utf-8
def is_odd(i):
	return(i%2==1)
L=[1,2,3,4,5,6,7,8,9]
print(filter(is_odd,L))
def not_blank(s):
	return(s and s.strip())
print(filter(not_blank,['A','b','',None,'  ','r']))
#用filter求素数
def odd_iter():
	n=1
	while True:
		n=n+2
		yield n
def not_devisible(n):
	return lambda x:x%n>0
def primes():
	yield 2
	it=odd_iter()
	while True:
		n=next(it)
		yield n
		it=filter(not_devisible,it)
#回数
def is_palindrome(i):
	return(str(i)[:])==(str(i)[::-1])#str(i)[::-1]可以表示倒序
print(filter(is_palindrome, range(1, 1000)))