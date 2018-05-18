import itchat
itchat.auto_login(hotReload=True)
users = itchat.search_friends(name = '海纯')
if users:
	UserName=users[0]['UserName']
	itchat.send('高兴啊',UserName)
else:
	print('查无此人')