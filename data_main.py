# coding: utf-8

"""
    项目功能
        1、解析http请求，组成查询sql
        2、连接hive执行查询,将结果封装到list中
        3、连接ftp,推送查询结果
"""
import data_tools as tools
#str = tools.linkHive("this is hello world!")
#str = tools.linkFtpTest('4')
#print(str)

#tools.fileHandle('E:/ftp/wo')
#str1 = tools.linkFtp(str)
#print(str1)
tools.linkOracle()