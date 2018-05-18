#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

def MailSender(SenderName,ReceiverAddr,Subject,Content):
	my_sender='XXXX@qq.com'
	my_pass = 'XXXX'#口令，不是密码，通常为16位字符串
	msg=MIMEText(Content,'plain','utf-8',)
	msg['From']=formataddr([SenderName,my_sender])
	msg['To']=formataddr(ReceiverAddr)
	msg['Subject']=Subject
	server=smtplib.SMTP_SSL("smtp.qq.com", 465)
	server.login(my_sender, my_pass)
	server.sendmail(my_sender,ReceiverAddr,msg.as_string())
	server.quit()
	print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'邮件发送成功')

ReceiverAddr=['XXX@live.com','XXX@qq.com']
SenderName='SenderName'
Subject='Subject'
Content='TestContent'
MailSender(SenderName,ReceiverAddr,Subject,Content)