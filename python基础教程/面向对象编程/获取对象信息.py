#coding=utf-8 
#判断对象类型可以使用type()
print(type(123))
print(type('123'))
print(type(abs))
#还可以输出布尔
print(type(123)==int)
print(type('123')==str)
print(type('abc')==type(abs))
#判断class类型使用isinstance()
class animal():
	def __init__(self):
		pass
class dog(animal):
	def __init__(self):
		pass
class husky(dog):
	def __init__(self):
		pass
a=animal()
d=dog()
h=husky()
print('-----------')
print(isinstance(a,animal))
print(isinstance(d,dog))
print(isinstance(h,husky))
print(isinstance(h,animal))
print(isinstance(h,object))
#获得一个对象的所有属性和方法，可以使用dir()函数
print(dir(a))
print(dir(123))
print('-------------')
print(dir('abc'))
print('ABC'.lower())
class MyObject():
	def __init__(self,x):
		self.x=x
	def power(self): 
		return(self.x*self.x)
obj=MyObject(10)
print('-------------')
print(hasattr(obj,'x'))
print(obj.x)
print(obj.power())
print(hasattr(obj,'y'))
setattr(obj,'y',123)
print(hasattr(obj,'y'))
print(obj.y)
getattr(obj,'y')
print(hasattr(obj,'power'))
fn=getattr(obj,'power')
print(fn)
print(fn())
inputmethod=obj.power()
if hasattr(obj,inputmethod):#看教程说可以用hasattr判断类中有没有可以使用的方法，但是自己操作却不能这么判断
	pass
else:
	pass