#coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time

class MailSender(object):
	def __init__(self,my_sender,my_pass,SenderName,Subject,Content):
		self.my_sender=my_sender
		self.my_pass=my_pass#口令，不是密码，通常为16位字符串
		self.SenderName=SenderName
		self.Subject=Subject
		self.Content=Content
	def SendIt():
		my_sender=self.my_sender
		my_pass =self.my_pass
		msg=MIMEText(Content,'plain','utf-8',)
		msg['From']=formataddr([SenderName,my_sender])
		msg['To']=formataddr(ReceiverAddr)
		msg['Subject']=Subject
		server=smtplib.SMTP_SSL("smtp.qq.com", 465)
		server.login(my_sender, my_pass)
		server.sendmail(my_sender,ReceiverAddr,msg.as_string())
		server.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'邮件发送成功')

my_sender='XXX@qq.com'
my_pass='XXXXXX'
ReceiverAddr=['XXX@live.com','XXX@qq.com']
SenderName='SenderName'
Subject='Subject'
Content='TestContent'
MailSender=MailSender(my_sender,my_pass,SenderName,ReceiverAddr,Subject,Content)
MailSender.SendIt()