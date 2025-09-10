'''
time() 获取当前时间戳
localtime(sec) 获取指定时间戳对应的本地时间的struct_time对象
ctime() 获取当前时间戳对应的易读字符串
strftime() 格式化时间, 结果为字符串
strptime() 提取字符串的时间, 结果为struct_time对象
sleep(sec) 使线程休眠sec秒
'''
import time
now = time.time() # 时间戳: 距离1970.1.1 08的秒数
print(now)

obj = time.localtime(0)
print(obj)
obj_now = time.localtime() # 默认值参数为当前时间戳
print(f"Year:{obj_now.tm_year} Month:{obj_now.tm_mon} Day:{obj_now.tm_mday} DOW:{obj_now.tm_wday}") # 0是星期一
print(f"Hour:{obj_now.tm_hour} Min:{obj_now.tm_min} Sec:{obj_now.tm_sec}")
# tm_yday: 今年的第几天
print(time.ctime()) # 时间戳对应的易读字符串

# 日期时间格式化. string format
print(time.strftime("Current time: %Y-%m-%d %H:%M:%S", time.localtime()))
# %B: 月名. 如January %A: 星期名. 如Wednesday

# 日期转struct_time
print(time.strptime("2008-08-08", "%Y-%m-%d")) # 未指定默认为0

time.sleep(5)
print('this is printed 5 sec later')