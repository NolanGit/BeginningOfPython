#coding=utf-8 
#tuple 调用数组的第X个元素的时候使用的语法是tuplename[0]表示取tuple每一组数据的第一个元素，见sorted
#string 切片的时候，倒序切片可以使用stringname[::-1]
for i in range(1,4):
	print i#打印的是123

def set_gender(self,gender):
		if (gender in('male','female')):
			self.__gender=gender
		else:
			raise ValueError('Bad gender')

#利用闭包返回一个计数器函数，每次调用它返回递增整数
def createCounter():
	i=[0]
	def counter():
		i[0]+=1
		return i[0]
	return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
	print('测试通过!')
else:
	print('测试失败!')