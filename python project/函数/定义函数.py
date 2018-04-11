
def my_abs(x):
	if not isinstance(x,int):
		raise TypeError('bad input')
	if x>0:
		return x
	elif x==0:
		return 0
	else:
		return -x
a=input()#因为input的输入类型是str，所以目前有瑕疵
print(my_abs(a))