
# 字符、字符串均可以用'_'/'''_'''/"_"/"""_"""表示，三重可以换行; print输出字符串默认为'_'
# ord() 字符转Unicode
# chr() Unicode转字符
# print(a,b) 输出时中间缺省加空格，末尾缺省加'\n'
print('a', ord("b")) # 打印字符串不会打出引号
print(chr(0x4e00))
print("""Characters_
    And""") # 仅三重引号表示的字符串可以换行，且换行符、前面的缩进会被打出来

# \也可以用来换行给代码换行，后面不能加任何东西，空格也不行
# 换行符不会被打出来，但是前面的缩进会被打出来
print("Characters_\
    And")

# 修改分隔符与结束符，见下
print(50,100,sep=',',end='')

# 字符(串)连接符 +
print('\n'+"50")

# 比C简单许多的文件操作
fp = open("test.txt",'w')
print("To C or not to C.", file = fp) # 会打换行符，这是由于print缺省end='\n'
fp.close()

# ------------------> print()里啥都能放，任何对象