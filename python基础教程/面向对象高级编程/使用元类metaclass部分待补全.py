#coding=utf-8
class Hello(object):
	def hello(self,name='world'):
		print('Hello %s' %name)
h=Hello()
h.hello()
print(type(Hello()))
print(type(h))
#type()既可以返回一个对象的类型，也可以创建一个新的类型,需要传入三个参数
#动态语言支持代码运行期间创建类
def fn(self,name='world'):
	print('Hello %s'%name)
Hello=type('Hello',(object,),dict(hello=fn))#class名称，所继承的父类集合(注意有一个逗号），所具有方法集合（这里把fn方法绑定到hello上）
print(type(Hello()))
print(type(h))
#metaclass
class Field(object):
	def __init__(self,name,colum_type):
		self.name=name
		self.colum_type=colum_type
	def __str__(self):
		return('<%s:%s>' %(self.__class__.__name__,self.name))
class StringField(Field):
	def __init__(self,name):
		super(StringField,self).__init__(name,'varchar(100)')
class IntegerField(object):
	def __init__(self, name):
		super(IntegerField, self).__init__(name,'bigint')
class ModelMetaclass(type):
	def __new__(cls,name,bases,attrs):
		