# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : file_rename
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
make 0460_m17_ms_12.pdf to 0460_17m_ms_12.pdf
"""

# History:
# 2022/1/25: Create
import os
import sys

if __name__ == '__main__':
    file_path = sys.argv[1]
    os.chdir(file_path)
    for file in os.listdir("."):
        if os.path.splitext(file)[1] == ".pdf":
            name_list=os.path.splitext(file)[0].split("_")
            new_yearname = name_list[1][1:]+name_list[1][:1]
            name_list[1] = new_yearname
            new_name = "_".join(name_list)
            os.rename(file,new_name+".pdf")
