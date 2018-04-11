#coding=utf-8
#一个子类可以继承多个父类
class Animal(object):
	pass
class Mammal(Animal):
	pass
class Bird(Animal):
	pass
class Runnable(object):
	pass
class Flyable(object):
	pass
class Dog(Mammal,Runnable):#一个子类就可以同时获得多个父类的所有功能
	pass
class Panda(Mammal,Runnable):
	pass
class Bat(Bird,Flyable):
	pass
class Eagle(Bird,Flyable):
	pass
print(Eagle.__mro__)
'''
mro:解析方法调用的顺序
把继承关系先构成一张图
利用拓扑排序的方法输出拓扑顺序，并列关系时遵循取最左原则
python继承顺序遵循C3算法，只要在一个地方找到了所需的内容，就不再继续查找
'''