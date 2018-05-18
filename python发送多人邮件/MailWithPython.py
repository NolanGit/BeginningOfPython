#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time
my_sender='XXXX@qq.com'
my_pass = 'XXXX'
my_user=['XXX@live.com','XXX@qq.com']
msg=MIMEText('XXXX','plain','utf-8',)
msg['From']=formataddr(["GoldMonitor",my_sender])
msg['To']=formataddr(my_user)
msg['Subject']="GoldPrice"
server=smtplib.SMTP_SSL("smtp.qq.com", 465)
server.login(my_sender, my_pass)
server.sendmail(my_sender,my_user,msg.as_string())
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'邮件发送成功')
server.quit()
print('done')