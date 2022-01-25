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

import Resources.config as config
import xlrd  # 导入库




if __name__ == '__main__':
    file = config.score_file

    # 打开文件
    xlsx = xlrd.open_workbook(file)
    # 查看所有sheet列表
    print('All sheets: %s' % xlsx.sheet_names())

    sheet1 = xlsx.sheets()[0]  # 获得第1张sheet，索引从0开始
    sheet1_name = sheet1.name  # 获得名称
    sheet1_cols = sheet1.ncols  # 获得列数
    sheet1_nrows = sheet1.nrows  # 获得行数
    print('Sheet1 Name: %s\nSheet1 cols: %s\nSheet1 rows: %s' % (sheet1_name, sheet1_cols, sheet1_nrows))

    sheet1_nrows4 = sheet1.row_values(3)  # 获得第4行数据
    sheet1_cols2 = sheet1.col_values(2)  # 获得第3列数据
    cell23 = sheet1.row(2)[3].value  # 查看第3行第4列数据
    print('Row 3: %s\nCol 2: %s\nCell 1: %s\n' % (sheet1_nrows4, sheet1_cols2, cell23))

    for i in range(sheet1_nrows):  # 逐行打印sheet1数据
        print(sheet1.row_values(i))