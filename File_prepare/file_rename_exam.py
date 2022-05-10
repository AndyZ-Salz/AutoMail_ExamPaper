# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : file_rename
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create
import os
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    exam_name = sys.argv[2]
    os.chdir(file_path)
    for file in os.listdir("."):
        if os.path.splitext(file)[1] == ".pdf":
            new_name=os.path.splitext(file)[0].split("_")[0]
            os.rename(file,new_name+exam_name+".pdf")
