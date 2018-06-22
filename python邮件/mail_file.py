#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    part = MIMEApplication(open('C:\\Users\\sunhaoran\\JustForFun.txt', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="JustForFun.txt")
    msg.attach(part)

    smtp = smtplib.SMTP_SSL()
    smtp.connect(smtpHost, '465')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    print("发送成功！")
    smtp.quit()

try:
    subject = 'Python 测试邮件'
    content = '这是一封来自 Python 编写的测试邮件。'
    send_email('smtp.qq.com', 'XXX@qq.com', 'XXX', 'XXX@live.com', subject, content)
except Exception as err:
    print(err)
