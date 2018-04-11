#coding=utf-8 
#使用一般程序写的限制条件
class Student1(object):
	
	def get_score(self):
		return self.score

	def set_score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value>100 or value<0:
			raise ValueError('bad value')
		self.score=value
#使用@property
class Student2(object):
	
	@property
	def score(self):
		return self.acore#这里必须把名字变一下，加下划线也可以，改一下名字也可以，因为如果不加的话调用实例的s.score的时候就会调用类的s.score，陷入了死循环

	@score.setter
	def score(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value>100 or value<0:
			raise ValueError('bad value')
		self.acore=value
s=Student2()
s.score=12
print(s.score)
#定义只读，即只设置getter不设置setter
class Student3(object):

	@property
	def birthyear(self):
		return self._birthyear

	@birthyear.setter
	def birthyear(self,value):
		if not isinstance(value,int):
			raise ValueError('score must be an integer')
		if value>3000 or value<1800:
			raise ValueError('bad value')
		self._birthyear=value

	@property
	def age(self):#2018
		return (2018-self.birthyear)
ss=Student3()
ss.birthyear=1995
print(ss.birthyear)
print(ss.age)