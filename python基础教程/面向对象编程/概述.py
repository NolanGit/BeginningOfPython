#coding=utf-8
#面向过程编程
std1={'name':'peter','score':98}
std2={'name':'marry','score':89}
print('%s:%s' %(std1['name'],std1['score']))
print('%s:%s' %(std2['name'],std2['score']))
#面向对象编程
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s' %(self.name,self.score))
robin=Student('robin',54)
alex=Student('alex',65)
robin.print_score()
alex.print_score()
