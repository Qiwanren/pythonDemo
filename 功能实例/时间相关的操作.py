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

