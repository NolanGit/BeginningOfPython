#【for循环】
#循环遍历数组,for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句
numbers=['1','2','3','4','5']
for number in numbers:
	print(number)
#range(X)可以生成从0-X的数组，从下边的例子可以看出range(X)生成的就是一个数组
sum=0
for x in range(101):
	sum=sum+x
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for l in L:
    print(l)
#【while循环】python没有自增和自减
sum=0
n=99
while n>0:
	sum=sum+n
	n=n-1
print (sum)
#break和continue
n=0
sum=0
while n<101:
	if n>50:
		break
	print(n)
	n=n+1
	
n=0
sum=0
while n<101:
	n=n+1
	if n%2!=0:
		continue
	print(n)