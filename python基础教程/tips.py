#tuple 调用数组的第X个元素的时候使用的语法是tuplename[0]表示取tuple每一组数据的第一个元素，见sorted
#string 切片的时候，倒序切片可以使用stringname[::-1]
for i in range(1,4):
	print i#打印的是123


	
	def set_gender(self,gender):
		if (gender in('male','female')):
			self.__gender=gender
		else:
			raise ValueError('Bad gender')