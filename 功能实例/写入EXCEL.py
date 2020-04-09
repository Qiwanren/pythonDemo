import xlwt

count = 0
workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet Name1")
for each in range(0, 10):
    sheet.write(0, 0, '这是第一列')  # row, column, value
    sheet.write(0, 1, '这是第二列')
    sheet.write(0, 2, '这是第三列')
    count = count + 1
workbook.save('D:\data\python\excel\Excel_test1.xls')