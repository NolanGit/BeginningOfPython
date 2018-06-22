# coding=utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.utils import formataddr
import email.mime.multipart
import email.mime.text
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


class MailSender(object):

    def __init__(self, my_sender, my_pass, sender_name, receiver_addr, subject, content):
        self.my_sender = my_sender
        self.my_pass = my_pass  # 口令，不是密码，通常为16位字符串
        self.sender_name = sender_name
        self.receiver_addr = receiver_addr
        self.subject = subject
        self.content = content

    def send_it(self):
        msg = MIMEMultipart(self.content, 'plain', 'utf-8',)
        msg['From'] = formataddr([self.sender_name, self.my_sender])
        msg['to'] = '管理员'
        msg['Subject'] = self.subject
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)
        server.login(self.my_sender, self.my_pass)

        part = MIMEApplication(open('C:\\Users\\sunhaoran\\JustForFun.txt', 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename="JustForFun.txt")
        msg.attach(part)

        server.sendmail(self.my_sender, self.receiver_addr, msg.as_string())
        server.quit()
        print(time.strftime('%Y-%m-%d %H:%M:%S',
                            time.localtime(time.time())) + '邮件发送成功')


my_sender = '345753110@qq.com'
my_pass = 'kohdrckbrfoicahj'
ReceiverAddr = ['shr1213@live.com']
SenderName = 'SenderName'
Subject = 'Subject'
Content = 'TestContent'
MailSender = MailSender(my_sender, my_pass, SenderName,
                        ReceiverAddr, Subject, Content)
MailSender.send_it()
