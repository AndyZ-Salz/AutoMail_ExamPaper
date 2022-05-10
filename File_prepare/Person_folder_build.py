# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : Person_folder_build
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/4/25: Create


import xlrd  # 导入库
import os


def open_file(path):
    # 打开文件
    xlsx = xlrd.open_workbook(path)
    # 查看所有sheet列表
    # print('All sheets: %s' % xlsx.sheet_names())
    sheet1 = xlsx.sheets()[0]  # 获得第1张sheet，索引从0开始
    sheet1_name = sheet1.name  # 获得名称
    sheet1_cols = sheet1.ncols  # 获得列数
    sheet1_nrows = sheet1.nrows  # 获得行数
    print('Sheet1 Name: %s\nSheet1 cols: %s\nSheet1 rows: %s' % (sheet1_name, sheet1_cols, sheet1_nrows))

    return sheet1


def read_personal_info(worksheet,config):
    person_first = config.fisrt_person
    person_last = worksheet.nrows

    print("Load {0} person(s)' information".format(person_last - person_first))

    persons_list = []

    for i in range(person_first, person_last):
        person_data = {}
        # if __name__ == '__main__':
        #     print("person's raw data: " + str(worksheet.row_values(i)))

        person_raw_data = worksheet.row_values(i)
        # student number
        person_data["studentNumber"] = person_raw_data[config.studentNumber_in_col]

        # name
        person_data["name"] = person_raw_data[config.name_in_col]


        persons_list.append(person_data)
        del person_data

    # print("persons_list before return:" + str(persons_list))
    return persons_list

def build_personal_folder(list, target):

    for person in list:
        print(person)
        path = target+person
        # 判断路径是否存在
        isExists = os.path.exists(path)

        # 根据需要是否显示当前程序运行文件夹
        # print("当前程序所在位置为："+os.getcwd())

        if not isExists:
            os.makedirs(path)
            print(path + ' 创建成功')
        else:
            print(path + ' 目录已存在')


if __name__ == '__main__':
    import Resources.config_andy as config
    file = config.score_file
    worksheet = open_file(file)
    persons_list = read_personal_info(worksheet,config)
    print("persons_list:"+str(persons_list))

    folder_list = []
    for person in persons_list:
        folder_name = person['studentNumber']+"_"+person['name']
        folder_name = folder_name.replace(' ','_')
        folder_list.append(folder_name)

    print("folder_list:"+str(folder_list))

    target_path = r"/Users/kyzang/Desktop/person/"
    build_personal_folder(folder_list,target_path)