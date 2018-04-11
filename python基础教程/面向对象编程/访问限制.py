#coding=utf-8
class Student1(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		self.__name=name#双下划线开头是私有变量，首位双下划线是特殊变量，对于单个下划线开头的变量，意思是“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
		self.__score=score
	def set_name(self,name):
		self.__name=name
	def set_score(self,score):
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
	def get_name(self):
		print(self.__name)
	def get_score(self):
		print(self.__score)
bart=Student1('bart',80)
bart.get_name()
bart.get_score()
bart.set_score(90)
bart.get_score()
#bart.set_score(190)
class Student2(object):
	def __init__(self, name, gender):
		self.__name=name
		self.__gender=gender
	def set_name(self,name):
		self.__name=name
	def get_name(self):
		print(self.__name)
	def set_gender(self,gender):
		if (gender in('male','female')):
			self.__gender=gender
		else:
			raise ValueError('Bad gender')
	def get_gender(self):
		print(self.__gender)
peter=Student2('peter','male')
peter.get_name()
peter.get_gender()
peter.set_gender('female')
peter.get_gender()