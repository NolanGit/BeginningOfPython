#coding=utf-8 
dic={'a':1,'b':2,'c':3}
for aaa in dic:
	print(aaa)
for value in dic.values():
	print(value)
str1="ABCDE"
for abc in str1:
	print(abc)
#可以通过isinstance函数来判断是否可以迭代
'''
from collectiongs import Iterable
isinstance('AAAAA',Iterable)'''
for i,values in enumerate(['A','B','C']):#enumerate函数可以同时获得索引和值
	print(i,values)
#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def maxandmin(list):
	min=list[0]
	max=list[0]
	for element in list:
		if element>max:
			max=element
		if element<min:
			min=element
	return min,max
print(maxandmin([1,2,3,4,6,8,-1.2341,4,-7]))