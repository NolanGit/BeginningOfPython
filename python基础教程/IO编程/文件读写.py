#coding=utf-8
try:
	f=open('C:\\Users\\sunhaoran\\Documents\\GitHub\\BeginningOfPython\\README.md','r',encoding='UTF-8')
	print(f.read())
except:
	pass
finally:
	f.close()

with open('C:\\Users\\sunhaoran\\Documents\\GitHub\\BeginningOfPython\\README.md','r',encoding='UTF-8')as f:
	for line in f.readlines():
		print(line)

with open('C:\\Users\\sunhaoran\\Documents\\GitHub\\BeginningOfPython\\README.md','a',encoding='UTF-8')as f:
	f.write('Nice Python!')

with open('C:\\Users\\sunhaoran\\Documents\\GitHub\\BeginningOfPython\\README.md','r',encoding='UTF-8')as f:
	for line in f.readlines():
		print(line)

#请将本地一个文本文件读为一个str并打印出来：
fpath = r'C:\Windows\system.ini'

with open(fpath, 'r') as f:
    s = f.readlines()
    print(s)
