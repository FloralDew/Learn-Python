# time可以很容易表示时间, 但在表示时间间隔上不如datatime
'''
datetime 表示日期时间的类. 包含年月日时分秒微妙
timedelta 表示时间间隔的类
date 表示日期的类
time 表示时间的类
tzinfo 时区相关的类
'''
from datetime import datetime
nowdt = datetime.now() # 当前系统时间
print(nowdt)
dt2 = datetime(2020, 8, 8, 20, 0) # 不填的ms默认为0
print(type(dt2))
print(dt2.year, dt2.microsecond) # 还有别的

# 比较两个datetime类型对象的大小
labor_day= datetime(2028, 5, 1)
national_day= datetime(2028, 10, 1)
print(labor_day < national_day) # True
print(labor_day - national_day) # -153 days, 0:00:00

# 与字符串相互转换
nowdt_str = nowdt.strftime('%Y/%m/%d')
print(nowdt_str)
dt = datetime.strptime("20.48.00", "%H.%M.%S")
print(dt) # 1900-01-01 20:48:00