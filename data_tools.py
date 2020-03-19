# coding: utf-8

# link hive的依赖
from impala.dbapi import connect
# 连接ftp
from ftplib import FTP
# 引入临时文件
from tempfile import TemporaryFile,NamedTemporaryFile
import io
import cx_Oracle

import os

#根据规则解析请求字符串组成查询条件
def analysisRequest(request):
    print(request)
    return request

## 连接hive数据库，根据查询结果进行查询，并将结果封装到list中进行返回
def linkHive(queryStr):
   try:
       print(queryStr)
       conn = connect(host="10.162.192.22", port=10000, database="qwr", user="qwr", auth_mechanism="PLAIN")
       cursor = conn.cursor()
       str11 = 'insert overwrite local directory \'/home/lisz/qwr/wo\' SELECT * FROM qiwanren_test LIMIT 100'
       print(str11)
       cursor.execute(str11)
       # rs = linkFtp(cursor,rsStr)
       ##查询结果为list
       return 'success'
   except Exception as  e:
       print("hive query exception!")

## 遍历list，并将结果list写入到ftp文件中
def linkFtp(cursor,resCount):
    ftp = FTP()  # 设置变量
    FILE_EXIST_FLAG = 0;
    RESULT_FILE_NAME = "1111111";
    buffer_size = 1024  # 每次从ftp获取数据大小
    #ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    try:
        ftp.connect("192.168.1.246", 21)  # 连接的ftp sever和端口
        ftp.login("Administrator", "admin")  # 连接的用户名，密码
    except FTP.error_perm:
        print("ERROR: cannot login anonymously")
    ftp.cwd("wo")  # 设置FTP当前操作的路径  ftp.cmd("xxx/xxx")
    # 检查文件是否存在
    fileList = ftp.nlst()   # ['6jack', 'OpenBSD']  返回一个文件列表
    for i in range(len(fileList)):
        if "1111111.txt" == fileList[i]:
            FILE_EXIST_FLAG = 1
    if FILE_EXIST_FLAG == 1:
        resultStr = "the reqId is exist!!"
    else:
        print("-------------begin to write file-------------------")
        # 用文件描述符来操作临时文件
        f = TemporaryFile()
        #将总数写入文件第一行
        bytestr = bytes(resCount+'\r\n', encoding='utf-8')
        f.write(bytestr)
        #将字符串转换为字节数组
        results = cursor.fetchall()
        for i in range(len(results)):
            #print("序号：%s   值：%s" % (i + 1, results[i][1]))
            rsStr = str(results[i][0]) +'|'+ results[i][1] +'|'+ str(results[i][2]) +'\r\n';
            bytestr = bytes(rsStr, encoding='utf-8')
            f.write(bytestr)
            f.seek(0)  # 从头读取，和一般文件对象不同，seek方法的执行不能
            # storbinary 文件不存在会自动创建，文件存在，则追加
            ftp.storbinary('STOR '+RESULT_FILE_NAME+"temp.txt",f,buffer_size)
        ftp.rename(RESULT_FILE_NAME+"temp.txt",RESULT_FILE_NAME+".txt") # 将fromname修改名称为toname。
        resultStr = "success"

    return resultStr


## 遍历list，并将结果list写入到ftp文件中
def linkFtpTest(resCount):
    ftp = FTP()  # 设置变量
    FILE_EXIST_FLAG = 0;
    RESULT_FILE_NAME = "1111111";
    buffer_size = 1024  # 每次从ftp获取数据大小
    #ftp.set_debuglevel(2)  # 打开调试级别2，显示详细信息
    try:
        ftp.connect("192.168.1.246", 21)  # 连接的ftp sever和端口
        ftp.login("Administrator", "admin")  # 连接的用户名，密码
    except FTP.error_perm:
        print("ERROR: cannot login anonymously")
    ftp.cwd("wo")  # 设置FTP当前操作的路径  ftp.cmd("xxx/xxx")
    # 检查文件是否存在
    fileList = ftp.nlst()   # ['6jack', 'OpenBSD']  返回一个文件列表
    for i in range(len(fileList)):
        if "1111111.txt" == fileList[i]:
            FILE_EXIST_FLAG = 1
    if FILE_EXIST_FLAG == 1:
        resultStr = "the reqId is exist!!"
    else:
        print("-------------begin to write file-------------------")
        f = io.BytesIO()  # ready for writing
        str = 'hello world!'
        str = str.encode(encoding='UTF-8', errors='strict')
        f.write(str)
        f.seek(0)  # 从头读取，和一般文件对象不同，seek方法的执行不能
        # storbinary 文件不存在会自动创建，文件存在，则追加
        print("f = " ,type(f))
        ftp.storbinary('STOR '+RESULT_FILE_NAME+'temp.txt',f,buffer_size)
        ftp.rename(RESULT_FILE_NAME+"temp.txt",RESULT_FILE_NAME+".txt") # 将fromname修改名称为toname。
        resultStr = "success"

    return resultStr


def linkOracle():
    print("begin to link oracle!")
    conn = cx_Oracle.connect('ubase/Wjs3Gfzgh@10.162.65.120:5901/orcl')  # 用自己的实际数据库用户名、密码、主机ip地址 替换即可
    curs = conn.cursor()
    sql = 'SELECT * FROM ts_test_info '  # sql语句
    rr = curs.execute(sql)
    row = curs.fetchone()
    print(row[0])
    curs.close()
    conn.close()

def fileHandle(filePath):
    for maindir, subdir, file_name_list in os.walk(filePath):
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            apath1 = os.path.join(maindir, 'wo_reqid.txt')  # 合并成一个完整路径
            fc = len(["" for line in open(apath, "r")])
            print("文件条数为：" + str(fc))
            os.rename(apath, apath1)