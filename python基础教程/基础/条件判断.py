# coding=utf-8
'''
# if 和else后边都有冒号，利用缩进来判断，如果判断为ture，则把缩进的两行执行了
i = 9
if i > 10:
    print('i=', i)
    print('i>10')
else:
    print('i=', i)
    print('i<10')
# else if 缩写为elif
print('input age')
age = input()  # 【输入的时候需要进行类型转换，因为input()返回的数据类型是str】
age = int(age)
if age < 10:
    print('kid')
elif 10 < age < 20:
    print('teenager')
else:
    print('adult')
# 另一种写法
x = input()
if x:
    print('ture')
'''
if (2 > 1 or 1 > 2 or 1 > 3) and 3 > 4:
    print('ok')
else:
    print('not ok')
