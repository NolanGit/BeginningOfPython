#coding=utf-8 
class Student1(object):
	def __init__(self,name):
		self.name=name
s=Student1('peter')
s.score=0
print(s.name)

class Student2(object):
	name='usualname'
	def __init__(self):
		pass
s=Student2()
s.score=0
print(s.name)
a=Student2()
a.name='biggerone'#实例属性优先级更高，会屏蔽掉类属性
print(a.name)

class Student3(object):
	"""docstring for Student3"""
	count=0
	def __init__(self, name):
		self.name=name
		Student3.count+=1
a=Student3('barney')
b=Student3('badass')
c=Student3('joey')
print(Student3.count)