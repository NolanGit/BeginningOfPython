#coding=UTF-8 
#要生成[1x1, 2x2, 3x3, ..., 10x10]
'''普通方法'''
def xxx(x):
	return x*x
L=[]
for x in xrange(1,11):
	L.append(xxx(x))
print L
'''列表生成式'''
print([x*x for x in range(1,11)])
#还可以过滤
print([x+1 for x in range(1,11) if x%2==0])#过滤出2、4、6、8、10然后加1，输出3、5、7、9、11
#两层或更多循环
print([a+b for a in 'ABC' for b in 'XYZ'])
#和dict结合
dic={'A':1,'B':2,'C':3}
print([a+str(b) for a,b in dic.items()])
#还可以直接放函数的返回值
L=['Hello','wORLD']
print([l.lower() for l in L])
#使用内建的isinstance函数可以判断一个变量是不是字符串：
L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s,str)])# if 判断的本身就是布尔表达式，所以没必要==Ture