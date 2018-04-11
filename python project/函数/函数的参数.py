#coding=utf-8

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数

def power(x,n=2):#默认为计算X的2次方，但也可以自定义N
	i=1
	a=x
	while i<n:
		x=x*a
		i=i+1
	return x
print(power(2,3))
#【注意】：必选参数在前，默认参数在后
def enroll(name,gender,age=20,city='beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
enroll('xiaoming','male',city='changchun')#可以越过age直接赋值city，但是要写变量名
#默认参数必须指向不变对象！
def add_end(L=[1]):
	L.append('end')
	print(L)
add_end([1,2,3])
add_end()
add_end()
add_end()

def calc(number):
	sum=0
	for n in number:
		sum=sum+power(n)
	return sum
print calc([1,2,3,4])#如果不用可变参数，需要将传入数据设置为list或tuple
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
def better_calc(*number):
	sum=0
	for n in number:
		sum=sum+power(n)
	return sum
print(better_calc(1,2,3,4))#使用可变参数可以避免数据类型转换
#关键字参数
def person(name,age,**kw):
	print('name:',name,'age:',age,'other:',kw)
person('Peter',12,company='inspur',phone='apple')
#一个*接收tuple，两个*接收dict
#如果需要限制接收到的关键字参数的名字，就要使用命名关键字参数
def person2(name,age,*,city,zipcode):
	print(name,age,city,zipcode)
#命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错
