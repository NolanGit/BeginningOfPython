#coding=utf-8 
#取list的前三个元素，注意包括的是0、1、2，而3没有包括
AA=['A','B','C','D','E']
print(AA[0:3])
#还可以倒序切片
print(AA[-2:-1])#输出的是D，同样也是不包括-1元素也就是E的
L=list(range(100))
print(L)
print(L[::5])#每隔5取一个，这个相当于是L[0:0:5],L[0:0]是选择全部的数据
print(L[0:50:3])
#利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(str):
	if str[:1]==' ':
		return trim(str[1:])
	elif str[-1:]==' ':
		return trim(str[:-1])
	return str
print(trim('   i\'m  good '))