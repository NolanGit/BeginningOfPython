#coding=utf-8
from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

s=StringIO('Nice Python\nisn\'t it?')
while True:
	a=s.readline()
	if a=='':
		break
	print(a.strip())