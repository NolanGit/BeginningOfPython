#coding=utf-8 
class Student(object):
	pass
s=Student()
s.name='bart'
print(s.name)
def set_age(self,age):
	self.age=age
from types import MethodType
s.set_age=MethodType(set_age,s)#给实例绑定方法
s.set_age(12)#尝试调用绑定的方法
print(s.age)#动态
#__slots__可以限制给实例增加的属性范围【对继承的子类不起作用,除非子类也使用一个slots，子类的属性才被限制为父类的slots加上子类的slots】
class employee(object):
	__slots__=('name','work')
e=employee()
#e.play='i want to play!'#报错
e.name='n.s'
e.work='work hard'
print(e.name)
print(e.work)

class AwesomeEmployee(employee):
	pass
ae=AwesomeEmployee()
ae.play='i can play!'
print(ae.play)

class BadEmployee(employee):
	__slots__=()
be=BadEmployee()
#be.play='i cant play'#报错
be.work='i just work....'#这个属性是父类定的，因为子类定了shots，所以他的属性范围为子类shots+父类shots
print(be.work)
