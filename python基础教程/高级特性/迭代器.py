#coding=utf-8 
#可以用函数isinstance()判断是否为Iterable可迭代对象
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance('abc',Iterable))
print(isinstance({},Iterable))
'''而生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值,称为iterator
可以用函数isinstance（xxx，iterable）来判断是否为迭代器
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，
直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，
只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。