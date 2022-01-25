# -*- coding: utf-8 -*-
"""
---------------------------------------
@file    : score_load
@Version : ??
@Author  : Andy Zang
@software: PyCharm
@For     : Auto_Mail
---------------------------------------
"""

# History:
# 2022/1/25: Create

import xlrd  # 导入库


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


def read_question_title(worksheet,config):
    title_start = config.question_start
    if config.question_in_last_col == True:
        title_finish = worksheet.ncols
    elif config.question_in_last_col == False:
        title_finish = worksheet.ncols - 1

    title_list = []
    index = 0
    for i in range(title_start, title_finish):
        title_data = {}
        title_data["question_index"] = index
        index += 1
        display_level = worksheet.row_values(0)[i]
        title_data["display_level"] = display_level
        question_title = worksheet.row_values(1)[i]
        title_data["question_title"] = question_title
        question_total_value = worksheet.row_values(2)[i]
        title_data["question_total_value"] = question_total_value
        title_list.append(title_data)

    if __name__ == '__main__':
        print("Question data will like: " + str(title_list))

    return title_list


def read_personal_results(worksheet, title_list,config):
    person_first = config.fisrt_person
    person_last = worksheet.nrows

    print("Load {0} person(s)' score".format(person_last - person_first))

    persons_list = []

    for i in range(person_first, person_last):
        person_data = {}
        # if __name__ == '__main__':
        #     print("person's raw data: " + str(worksheet.row_values(i)))

        person_raw_data = worksheet.row_values(i)
        # name
        person_data["name"] = person_raw_data[config.name_in_col]

        # email address
        person_data["mail"] = person_raw_data[config.mail_in_col]

        # real_score
        title_start = config.question_start
        if config.question_in_last_col == True:
            title_finish = worksheet.ncols
        elif config.question_in_last_col == False:
            title_finish = worksheet.ncols - 1

        index = 0
        person_score = []
        for j in range(title_start, title_finish):
            real_score = person_raw_data[j]
            if real_score == '':
                real_score = 0.0

            question_score ={}
            question_score['question_index'] = title_list[index]['question_index']
            question_score['display_level'] = title_list[index]['display_level']
            question_score['question_title'] = title_list[index]['question_title']
            question_score['question_total_value'] = title_list[index]['question_total_value']
            question_score["real_score"] = real_score
            index += 1
            person_score.append(question_score)

        # if __name__ == '__main__':
        # print("person's score data: " + str(person_score))

        person_data["score"] = person_score
        del person_score

        # note
        if config.question_in_last_col == False:
            person_data["note"] = person_raw_data[worksheet.ncols - 1]

        if __name__ == '__main__':
            print("Personal data after processing：" + str(person_data))

        persons_list.append(person_data)
        del person_data

    # print("persons_list before return:" + str(persons_list))
    return persons_list


if __name__ == '__main__':
    import Resources.config_andy as config
    file = config.score_file
    worksheet = open_file(file)
    title_list = read_question_title(worksheet,config)
    persons_list = read_personal_results(worksheet, title_list,config)


    # print("final:" + str(persons_list))

    # sheet1_nrows4 = sheet1.row_values(3)  # 获得第4行数据
    # sheet1_cols2 = sheet1.col_values(2)  # 获得第3列数据
    # cell23 = sheet1.row(2)[3].value  # 查看第3行第4列数据
    # print('Row 3: %s\nCol 2: %s\nCell 1: %s\n' % (sheet1_nrows4, sheet1_cols2, cell23))

    # for i in range(sheet1_nrows):  # 逐行打印sheet1数据
    #     print(sheet1.row_values(i))
