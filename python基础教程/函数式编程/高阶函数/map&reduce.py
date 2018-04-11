#coding=utf-8 
#高阶函数就是将函数作为参数传递到函数里边
#map就是依次将参数传入所写的函数，然后输出结果
from __future__ import division  
from collections import Iterator
def f(x):
	return 3.14*x*x
s=map(f,[1,2,3,4,5,6,7,8,9,10])
print(isinstance(s,Iterator))
print(map(str,[1,2,3,4,5]))
from functools import reduce
def multiply(a,b):
	return(a*b)
print (reduce(multiply,[1,2,3,4,5,6,7,8,9,10]))
#char2num
def function(a,b):
	return(a*10+b)
def getnum(s):
	dict={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
	return dict[s]
print(reduce(function,map(getnum,'12341234')))
#整理成一个
def str2num(s):
	dict={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
	def function(a,b):
		return a*10+b
	def getnum(s):
		return dict[s]
	return(reduce(function,map(getnum,s)))	
print(str2num('123123'))
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):#有bug，输出的不是单词string
	dict1={'a':'A','b':'B','c':'C','d':'D','e': 'E', 'f': 'F', 'g': 'G', 'h': 'H', 'i': 'I', 'j': 'J','k': 'K', 'l': 'L', 'm': 'M', 'n': 'N', 'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T','u': 'U', 'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z','A':'A','B':'B','C':'C','D':'D','E': 'E', 'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J','K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T','U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 'Z': 'Z'}
	dict2={'A':'a','B':'b','C':'c','D':'d','E': 'e', 'F': 'f', 'G': 'g', 'H': 'h', 'I': 'i', 'J': 'j','K': 'k', 'L': 'l', 'M': 'm', 'N': 'n', 'O': 'o ', 'P':'p', 'Q': 'q', 'R': 'r', 'S': 's', 'T': 't','U': 'u', 'V': 'v', 'W': 'w', 'X': 'x', 'Y': 'y', 'Z': 'z','a':'a','b':'b','c':'c','d':'d','e': 'e', 'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j','k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't','u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 'z': 'z'}
	def upperthefirst(name):
		return([dict1[name[:1]]]+[([dict2[name[i]]]) for i in range(1,len(name))])
	return (map(upperthefirst,name))
L1='adam', 'LISA', 'barT'
print(normalize(L1))
#str2float
def str2float(str):
	def multen(a,b):
		return a*10+b
	def divten(a,b):
		return a/10+b
	dict={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
	def getnum(s):
		return dict[s]
	i=0
	strtemp1=''
	strtemp2=''
	while True:
		if str[i]!='.':			
			strtemp1=strtemp1+str[i]
			i=i+1
		else:
			break
	while True:
		if i<(len(str)-1):
			i=i+1		
			strtemp2=str[i]+strtemp2
		else:
			break
	part1=reduce(multen,map(getnum,strtemp1))
	part2=(reduce(divten,map(getnum,strtemp2))/10)
	return part1+part2
print(str2float('112323.123213'))
#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
	def multiply(a,b):
		return(a*b)
	return(reduce(multiply,((L[i]) for i in range(0,len(L)))))
L=[3, 5, 7, 9]
print(prod(L))