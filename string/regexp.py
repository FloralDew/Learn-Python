# 正则表达式
'''
元字符
.   除了\n的任意字符
\w  字母数字下划线
\W  非字母数字下划线
\s  任意空白字符
\S  任意非空白字符
\d  任意十进制数

限定符：限定匹配的次数
?       0次或1次
+       1次或多次
*       0次或多次
{n}     n次
{n,}    最少n次
{n,m}   最少n次最多m次

其他字符
[]              区间
^               在区间中排除字符
|               匹配|左右的任意字符
\               转义字符，如\.
[\u4e00-\u9fa5] 任意汉字
()              改变结合顺序
'''

## 用re模块使用正则表达式
import re

# match() 从头开始匹配字符串
s = 'i study 3.13'
m = re.match('\d\.\d+', s, re.I)
print(m) # None
s2 = '3.13 i study'
m = re.match('\d\.\d+', s2, re.I)
print(m) # <re.Match object; span=(0, 4), match='3.13'> (0,4)不包括4

'''第三个参数Flag(缺省为0)说明：
re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
'''

# 取出m中的东西
print('start:', m.start())
print('end:', m.end())
print('区间:', m.span())
print('待匹配字符串:', m.string)
print('匹配的数据:', m.group())

# search() 搜索第一个匹配的值
s3 = 'l love 3.7.4 and 3.11'
m2 = re.search('\d\.\d+', s3) # 匹配不到则m2 = None
print(m2) # <re.Match object; span=(7, 10), match='3.7'>

# findall() 搜索全部匹配的值，返回.group()构成的列表
lst = re.findall('\d\.\d+', s3) # 找不到则返回空列表[]
print(lst)

# sub()
comment = 'Fuck you bitch'
new_s = re.sub('fuck|bitch|shit', '***', comment, 0, re.I)
# count参数表示要替换的最大次数。0表示全部
print(new_s)

# split
s4 = 'apple/banana&pear/ice'
lst2 = re.split('/|%|&', s4)
print(lst2)