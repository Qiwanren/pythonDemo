import datetime
import string
import random


#获得当前时间
now = datetime.datetime.now()
#转换为指定的格式:
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
## 生成一个随机数
seeds = string.digits
random_str = random.sample(seeds, k=3)
print("".join(random_str))


### 计算时间的差值
## 2019-11-30 23:46:14
str_p = '2019-01-30 15:29:08'
dateTime_p = datetime.datetime.strptime(str_p,'%Y-%m-%d %H:%M:%S')
print(dateTime_p) # 2019-01-30 15:29:08
