# requests
# 用于处理HTTP(超文本传输协议)请求的第三方库, 在爬虫中应用广泛
# 本.py使用requests爬取天气预报中的热门景点

import requests
# 使用get()打开网络请求, 获取response对象
url = 'https://www.weather.com.cn/weather1d/101020100.shtml' # 要使用爬虫打开的浏览器网页
resp = requests.get(url) # 相应对象
resp.encoding = 'utf-8' # 有中文, 设置编码
# print(resp.text) # 实例属性text. 爬取到的是url页面

# 使用正则表达式查找并提取景点推荐
import re
city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', resp.text) # \u4e00-\u9fa5: 汉字
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', resp.text)
wd = re.findall('<span class="wd">(.*)</span>', resp.text)
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', resp.text)

# 打包
lst = []
for a, b, c, d in zip(city, weather, wd, zs):
    lst.append([a, b, c, d])

print(lst)

# 以上代码拷贝一份存入module_get_attraction.py中, 供openpyxl使用.

# --------------------------------------------
# 以上使用.text爬取文本数据, 以下爬取二进制数据
url = 'https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png'
resp = requests.get(url)
with open('baidu_logo.png', 'wb') as file:
    file.write(resp.content)