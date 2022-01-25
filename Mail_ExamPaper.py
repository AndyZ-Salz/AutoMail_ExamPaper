# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Mail_ExamPaper
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create
import time

import Resources.config as config
import Resources.mail_templet as templet
import mail_auth as auth
import score_load
import mail_text_construct
import mail_send


def score_data_load(path):
    worksheet = score_load.open_file(path)
    title_list = score_load.read_question_title(worksheet,config)
    persons_list = score_load.read_personal_results(worksheet, title_list,config)

    return persons_list


if __name__ == '__main__':
    file = config.score_file
    print(file)
    persons_list = score_data_load(file)

    for person_data in persons_list:
        print(person_data)
        mail_text = mail_text_construct.mail_text_generator(person_data,config,templet) #text body
        print("Trying to send mail to "+ person_data["name"])
        print(mail_text)

        recevier = person_data["mail"]
        subject = "Score for " + config.exam_name

        # send mail
        mail_person = mail_send.Mail()
        mail_person.head_generator(auth.mail_user, recevier, subject)
        mail_person.server_config(auth.mail_host, auth.mail_port, auth.mail_user, auth.mail_pass, SSL=True)
        mail_person.body_generator(mail_text, "plain")
        mail_person.send_mail()

        #增加间隔
        time.sleep(2)

    print("Mail_Project {} finish".format(config.project_name))