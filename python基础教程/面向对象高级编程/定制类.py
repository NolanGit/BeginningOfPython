#coding=utf-8
class Student(object):
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return ('Student object (name:%s)' %self.name)
s=Student('bart')
print(s)#Student object (name:bart)
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须有一个__iter__()方法
'''报错
class Fib(object):
	def __init(self):
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a>1000:
			raise Stop()
		return self.a
for i in Fib():
	print i
'''
