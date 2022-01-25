# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : mail_text_construct
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create
import Resources.config as config
import Resources.mail_templet as templet
import score_load


def body_text_generator(person_data):
    body = templet.body.format(exam = config.exam_name)

    for question in person_data['score']:
        item = templet.space * int(question["display_level"]) + templet.score_item.format(
            question_title=question["question_title"],
            real_score=question["real_score"],
            question_total_value=question["question_total_value"],
        )
        body += item

    return body


def mail_text_generator(person_data):
    head = templet.head.format(receiver=person_data["name"])

    body = body_text_generator(person_data)

    sign = templet.sign

    acknowlege = templet.acknowlege

    return head + body + sign + acknowlege


if __name__ == '__main__':
    file = config.score_file
    worksheet = score_load.open_file(file)
    title_list = score_load.read_question_title(worksheet)
    persons_list = score_load.read_personal_results(worksheet, title_list)

    for person_data in persons_list:
        print(mail_text_generator(person_data))
