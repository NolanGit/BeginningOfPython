#coding=utf-8 
dict={'A':1,'B':2,'C':3}#其中A,B,C称为dict的key
print(dict['B'])
#dict必须使用不可变对象作为key
dict['A'] = 67

#删除dict使用pop()
#dict.pop(dict[1])
#print(dict)
#set可以看成数学意义上的无序和无重复元素的集合,使用list作为参数
s=set([1,2,3,4,5])
print(s)#{1, 2, 3, 4, 5}
s.add(6)
print(s)#{1, 2, 3, 4, 5，6}
s.add(6)
s.add(6)
s.add(6)
print(s)#{1, 2, 3, 4, 5，6}
s.remove(2)

grade={'A':78,'B':89,'C':100}
exit=input('input Y/N\n')
if exit=='Y':
	print('input the name ')
	name=input()
	if name in grade:
		print('%s grade is'%name,grade[name])