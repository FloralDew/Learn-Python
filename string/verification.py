# 对用户输入字符串进行合法性验证

# isdigit()只识别十进制阿拉伯数字
print('123'.isdigit()) # True
print('0b1001'.isdigit()) # False
print('一'.isdigit()) # False
print('I'.isdigit()) # False

# isnumeric可以识别十进制中文/罗马/阿拉伯数字
print('123'.isnumeric()) # True
print('伍万叁仟肆佰'.isnumeric()) # True
print('一'.isnumeric()) # True
print('ⅠⅡⅢ'.isnumeric()) # True

# 所有字符都是字母(包含中文字符)
print('hello你好'.isalpha()) # True
print('hello你好123'.isalpha()) # False
print('hello你好一二三'.isalpha()) # True
print('hello你好壹贰叁'.isalpha()) # True
print('hello你好ⅠⅡⅢ'.isalpha()) # False

# 所有字符都是数字或字母 isalnum()
# 所有字符都是小写 islower()
# 所有字符都是大写 isupper() 中文既是大写又是小写
# 每个单词有且仅首字母大写(以空格分隔单词) istitle()
# 是否都是空白字符
print('\t \n'.isspace()) # True
