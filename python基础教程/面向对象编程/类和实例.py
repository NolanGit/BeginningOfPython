#coding=utf-8 
class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.name=name
		self.score=score
	def print_score(self):
		print('%s:%s' %(self.name,self.score))
	def get_grade(self):
		if self.score>=90:
			print('A')
		elif self.score>=60:
			print('B')
		else:
			print('C')
robin=Student('robin',54)
alex=Student('alex',65)
robin.print_score()
alex.print_score()
robin.get_grade()
alex.get_grade()