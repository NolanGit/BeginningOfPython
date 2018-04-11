#coding=utf-8
#一般情况的求和函数
def calc_sum(*args):
	ax=0
	for n in args:
		ax=ax+n
	return ax
#返回函数
def lazy_sum(*args):
	def sum():
		ax=0
		for n in args:
			ax=ax+n
		return ax
	return sum
f=lazy_sum(1,2,3,4,5)#调用sum时候，返回的是函数
print(f)
print(f())#调用f时候，才返回结果
#在调用lazy_sum时候每次调用都会返回一个新的函数
f1=lazy_sum(1,2,3)
f2=lazy_sum(1,2,3)
print(f1==f2)#return false
#参数全部保存在返回的函数中
