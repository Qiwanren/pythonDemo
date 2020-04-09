import os

## 读取目录中的文件
filePath = 'C:\\Users\\Administrator\\Desktop\\SK\\dat\\'
fileList = []
for i,j,k in os.walk(filePath):
    fileList = k
for file in fileList:
    cmd_request = "sqlldr qwr/admin@192.168.31.245:1521/orcl control=C:\\Users\\Administrator\\Desktop\\SK\\wwdata2.ctl log=C:\\Users\\Administrator\\Desktop\\SK\\log.log data=C:\\Users\\Administrator\\Desktop\\SK\\dat\\"+file
    print(cmd_request)
    d = os.popen(cmd_request)
    print(d.read())

