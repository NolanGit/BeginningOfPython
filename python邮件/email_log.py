#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import time
import os
import sys
from email.utils import formataddr
print('发送邮件给' + sys.argv[1] + '....')


def send_email(smtpHost, sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    #msg['from'] = sendAddr
    msg['from'] = formataddr(['log', sendAddr])
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件
    '''
    rootdir = 'D:\\GCloud\\log\\dtdCheckOfCity'
    list = os.listdir(rootdir)

    for i in range(0, len(list)):
        path = os.path.join(rootdir, list[i])
        path = path.replace('\\', '/')
        part = MIMEApplication(open(path, 'rb').read())
        part.add_header('Content-Disposition', 'attachment', filename=list[i])
        msg.attach(part)
    '''
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
    subject = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '日常检查日志'
    content = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time())) + '附件为当前日志'
    send_email('smtp.qq.com', 'XXX@qq.com', 'XXX', sys.argv[1], subject, content)
except Exception as err:
    print(err)
