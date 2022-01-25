# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : mail_send
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.utils import formataddr


class Mail:
    def __init__(self):
        self.message = MIMEMultipart()
        self.__head_flag = 0
        self.__body_flag = 0
        self.__attach_flag = 0
        self.__server_flag = 0

    def head_generator(self, sender: str, receiver: str, subject: str, sendername: str = "", receivername: str = ""):
        self.__sender = sender
        self.__receiver = receiver
        self.message['From'] = formataddr((sendername, sender))
        self.message['To'] = formataddr((receivername, receiver))
        self.message['Subject'] = Header(subject, 'utf-8')
        self.__head_flag = 1

    def body_generator(self, body: str, body_type: str = None):
        if body_type == None:
            body_type = "plain"

        if body_type == "plain" or body_type == "html":
            self.message.attach(MIMEText(body, body_type, 'utf-8'))
            self.__body = body
            self.__body_flag = 1

        else:
            print("wrong body type")

    def body_check(self):
        if self.__body_flag == 0:
            print("No mail Body")
        else:
            print(self.__body)

    def attach_generator(self):
        pass

    def server_config(self, host: str, port: int, username: str, password: str, SSL=False):
        if SSL == False:
            self.__smtpObj = smtplib.SMTP(host, port)
        elif SSL == True:
            self.__smtpObj = smtplib.SMTP_SSL(host, port)
        self.__username = username
        self.__password = password
        self.__server_flag = 1

    def send_mail(self):
        if self.__head_flag == 0:
            print("Please set mail head!")
        elif self.__body_flag == 0:
            print("Please set mail body!")
        elif self.__server_flag == 0:
            print("Please set mail server!")
        else:
            try:
                self.__smtpObj.login(self.__username, self.__password)
                self.__smtpObj.sendmail(self.__sender, self.__receiver, self.message.as_string())
                print("邮件发送成功")
                self.__smtpObj.quit()

            except smtplib.SMTPException:
                print("Error: 无法发送邮件")


if __name__ == '__main__':
    import mail_auth as auth

    amail = Mail()
    amail.head_generator(auth.mail_user, "cc@dd.com", "Hi from python")
    amail.server_config(auth.mail_host, auth.mail_port, auth.mail_user, auth.mail_pass, SSL=True)
    amail.body_generator("HI", "plain")
    amail.send_mail()
