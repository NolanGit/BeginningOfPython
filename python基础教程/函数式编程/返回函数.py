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

#闭包
def count():
	fs=[]
	for i in range(1,4):
		def fn():
			return i*i
		fs.append(fn)
	return fs
func1,func2,func3=count()
print(func1(),func2(),func3())

#利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
	i=[0]
	def counter():
		i[0]+=1
		return i[0]
	return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
	print('测试通过!')
else:
	print('测试失败!')