# !/usr/bin/python3
# coding: utf-8

import xlrd as xlrd

## 读取xls文件内容
###   cell_lac_inuse  无主小区码表

print("开始文件数据读取···············")

xls_file = xlrd.open_workbook("D:\\file\data\\tmp\\nocell_tj.xls")
f = open('D:\\file\\data\\tmp\\result01.txt', 'w')

xls_sheet = xls_file.sheets()[0] ## 打开第一个sheet

rows = xls_sheet.nrows     ###  获取共有多少行数据

# 开始读取表数据
for i in range(rows):
	# row_values()  根据索引以列表形式返回一行数据
    row = xls_sheet.row_values(i)
    print(row)
    for j in range(int(row[5]),int(row[6])+1):
        strs = str(row[1]) + "," + row[3] + "," +str(j) + "," +str(row[4])+ ",20190702," +str(int(row[7]))
        f.writelines(strs)
        f.writelines("\n")

print("文件数据读取完成···············")
f.close()







