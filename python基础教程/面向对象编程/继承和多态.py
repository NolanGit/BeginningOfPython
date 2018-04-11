#coding=utf-8 
class Animal(object):
	"""docstring for Animal"""
	def __init__(self, name):
		self.__name=name
	def run(self):
		print('Animal is running')
	def eat(self):
		print('yummy')
class cat(Animal):
	def __init__(self):
		pass
	def run(self):
		print('cat is running')
cat=cat()
cat.run()
class dog(Animal):
	"""docstring for dog"""
	def __init__(self):
		pass
	def run(self):
		print('dog is running')
	def bark(self):
		print('dog is barking')
dog=dog()
def run_twice(animal):
	animal.run()
	animal.run()
print('-----------')
run_twice(cat)
run_twice(dog)
'''
多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。
由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思
'''
#传入run_twice的也不必须是animal，只要有run()的数据类型都可以传进去