#coding=utf-8
def foo(n):
	n=int(n)
	assert n!=0,"n is zero"
	return 10/n
foo(0)