import requests

def get_html(url):
    resp = requests.get(url) # 相应对象
    resp.encoding = 'utf-8' # 有中文, 设置编码
    return resp.text

# 使用正则表达式查找并提取景点推荐
import re
def parse_html(html_str):
    city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', html_str) # \u4e00-\u9fa5: 汉字
    weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', html_str)
    wd = re.findall('<span class="wd">(.*)</span>', html_str)
    zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', html_str)

    # 打包
    lst = []
    for a, b, c, d in zip(city, weather, wd, zs):
        lst.append([a, b, c, d])
    
    return lst