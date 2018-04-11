#coding=utf-8 
print('%s%s' %('hello',' python'))
print('%.2f' % 3.1415926)

i=0
print('%4f'%i)

print('%s%%' %'100')

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
a=72
b=85
c=(b-a)/a
print('{0:.11}%' .format(c))
#例句：print('Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125))