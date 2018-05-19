import itchat
itchat.auto_login(hotReload=True)
users = itchat.search_friends(name = 'NickName')
if users:
	UserName=users[0]['UserName']
	itchat.send('XXX',UserName)
else:
	print('查无此人')
#发送给文件传输助手itchat.send((time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))),'filehelper')