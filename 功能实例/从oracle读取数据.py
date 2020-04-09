import cx_Oracle
import xlwt
import csv

### 连接oracle数据库
conn = cx_Oracle.connect('qwr/admin@192.168.31.245/orcl')
cur = conn.cursor()
cur.execute("select t.rec_date from skww_vibeac_days t ")  # 查询数据内容
rows = cur.fetchall()  # 由于每条数据格式一样，只取一条内容格式来赋值
rowsList = list(rows)
for row in rowsList:  # 取出查询到的数值，并赋值给参数
    print(row[0])
    cur.execute("select t.msg_id,t.send_status,t.callback_status,t.send_request_time,t.callback_send_time,t.status_flag,t.day_flag from skww_data_pipei_ok_result t where t.rec_date = '"+row[0]+"'")  # 查询数据内容
    rows1 = cur.fetchall()
    rowsList1 = list(rows1)
    # 1. 创建文件对象
    save_name = "D:/data/python/excel/" + row[0] + ".csv"
    f = open(save_name, 'w', encoding='utf-8', newline='')
    # 2. 基于文件对象构建 csv写入对象
    csv_writer = csv.writer(f)
    # 3. 构建列表头
    ##消息ID，微位投递状态，时科回调状态，微位投递时间，时科回调时间，状态对比，时间对比
    csv_writer.writerow(["消息ID", "微位投递状态", "时科回调状态","微位投递时间","时科回调时间","状态对比","时间对比"])
    count = 0
    for row1 in rowsList1:
        # 4. 写入csv文件内容
        csv_writer.writerow([row1[0], row1[1], row1[2],row1[3],row1[4],row1[5],row1[6]])
    # 5. 关闭文件
    f.close()

'''
    写入excel文件中，有大小限制，每个只能写7万多
    for row in rowsList:  # 取出查询到的数值，并赋值给参数
    print(row[0])
    cur.execute("select t.Rec_Date,T.MSG_ID,T.STATUS_FLAG,T.DAY_FLAG from skww_vibeac_pipei_ok_result t where t.rec_date = '"+row[0]+"'")  # 查询数据内容
    rows1 = cur.fetchall()
    rowsList1 = list(rows1)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet(row[0])
    count = 0
    for row1 in rowsList1:
        sheet.write(count, 0, row1[0])  # row, column, value
        sheet.write(count, 1, row1[1])
        sheet.write(count, 2, row1[2])
        sheet.write(count, 3, row1[3])
        count = count + 1
    save_name = "D:/data/python/excel/" + row[0] + ".xls"
    workbook.save(save_name)

    
'''

'''


while rows is not None:
    f = open('FileTable.txt', 'a+')
    f.write(str(rows).lstrip('(').rstrip(')').replace(', ', '\t').replace("'", "") + '\n')
    rows = cur.fetchone()
cur.close()
conn.close()
'''