# 任何用引号引出的部分都是字符串
address = '上海市杨浦区邯郸路220号'
print(address)

# 三个单/双引号：多行字符串
info='''上海市杨浦区
    30号楼
    606
'''
print(info)

# 转义字符 \n \t \' \" \\
print('123456789')
print('1\t12345678') # 一个制表位是8个字符
print('12345678\t1')

# 原字符：使转义字符失效的符号r或R
print(R'123\n\'45678\t1') # 输出123\n\'45678\t1

# 字符串的索引: 0,1,.../...,-2,-1
s = 'helloworld'
print(s[1],'它的类型是',type(s[1]))

# 字符串的切片
print(s[1:2]) # 从1开始到2结束不包含2
print('helloworld'[-5:9]) # 不包含9
print(s[1:]) # 到结尾
print(s[-9:])
print(s[:4]) # 从头
print(s[:-6])

# 字符串的运算
x = '复旦大学'
y = '微电子爷'
# 连接 x + y
print(x + y)
# 复制n次 n * x 或 x * n
print(10 * y) # end = '\n' 只会加在最后
# 判断包含关系
print('微电子' in y) # True

## 字符串的方法
s = 'Helloworld'

# 大小写转换
print(s.lower()) # lower必须加括号
print(s.upper())

# 字符串的分割
s1 = 'apple/banana/pears'
lst = s1.split('/')
print(lst)

# 计数
print(s1.count('a'))

# 检索
print(s1.find('/'))
print(s1.find('z')) # 与.index作用相同，但find找不到会返回-1而不是报错

# 判断前缀和后缀
print(s1.endswith(('pears'))) # True
print(s1.startswith('Apple')) # False

# 替换
new_s = s.replace('o', '?')
print(new_s)
print(s.replace('o', '?', 1)) # 只替换第一个

# 在指定宽度居中
print(s.center(20))
print(s.center(20, '*')) # 两侧用*填充

# 去掉左右空格
s = '   helloworld     '
print(s.strip()) # 去掉左右空格
print(s.lstrip()) # 去掉左空格
print(s.rstrip()) # 去掉右空格

# 去掉左右指定字符
s = 'dlHelloworld'
print(s.strip('ld')) # 去掉左右
print(s.lstrip('lod')) # 去掉左
print(s.rstrip('dl')) # 去掉右
# 与strip实参字符串字母的顺序无关；中间的字符不会去掉

# 字符串格式化
# (1)占位符
s = 'res'
age = 19
score = 98.5
print('name:%s age:%d score:%.1f' % (s, age, score))

# (2)f-string
print(f'name:{s} age:{age} score:{score}')

# (3)format方法
print('name:{0} age:{1} score:{2}'.format(s, age, score))
# {0}{1}{2}对应format参数中的索引

# format的详细用法 :为格式引导符
s = 'helloworld'
print('{0:*<20}'.format(s)) # 字符串的显示宽度为20，左对齐<，空白部分用*填充
print('{0:0>20}'.format(s)) # 右对齐
print('{0:0^19}'.format(s)) # 居中对齐. 奇数则左边比右边少一个
print('{0:,}'.format(98765432)) # 三位一逗号 只能用于整数和浮点数
print('{0:,}'.format(98765432.9876)) # 小数不加逗号
print('{0:.2f}'.format(3.144)) # 保留两位小数(round)
print('{0:.2}'.format(s)) # 字符串截取前两个字符
# 整数的进制转换
print('bin:{0:b},dec:{0:d},oct:{0:o},hex:{0:x}'.format(0xa))
# 浮点数可以保留小数、转指数百分数
print('{0:.2f}, {0:.3e}, {0:.2%}'.format(3.14159))

## 字符串的编码和解码

# 编码 str->bytes 解码 bytes->str
s = 'helloworld你好世界'
scode = s.encode(errors = 'replace') # 默认utf-8编码，中文占3个字节
# strict：遇到无法转换的字符报错；ignore：忽略；replace：用?代替
print(scode, type(scode))
scode = s.encode('gbk', errors = 'replace') # gbk中中文为2个字节
print(scode, type(scode))

s1 = 'cheese✌'
scode1 = s1.encode('gbk', errors = 'ignore') # b'cheese'
print(scode1, type(scode1))
scode1 = s1.encode('gbk', errors = 'replace') # b'cheese?'
print(scode1, type(scode1))
# scode = s1.encode('gbk', errors = 'strict') # 报错 'gbk' codec can't encode character '\u270c' in position 6: illegal multibyte sequence
# print(scode, type(scode))

# 解码
print(bytes.decode(scode, 'gbk'))