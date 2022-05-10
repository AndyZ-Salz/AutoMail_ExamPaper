# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : mail_templet
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create

head = """
Dear {receiver}
"""

body_top = """
good morning!

Your scores in {exam} are as follows:
"""

space = "  "

score_item = """{question_title}: {real_score:.1f}/{question_total_value:.0f}
"""

body_bottom = """
"""

sign = """
Best wishes
Andy
"""

acknowlege = """
This email contains content generated by a Python script, I apologize for any errors in advance.
"""

if __name__ == '__main__':
    print(head.format(receiver="andy") + body_top + body_bottom + sign + acknowlege)
