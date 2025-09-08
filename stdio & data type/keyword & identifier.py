# Python的保留字和C的关键字一样，不能作为变量或函数名，如and/is/in...

import keyword # Python解释器自带的keyword模块可以用来查询保留字

print(keyword.kwlist) # 打印保留字列表
print(len(keyword.kwlist)) # len用于计算容器中元素个数

#保留字、标识符严格区分大小写
true = '真' # 正确，因为True才是Python保留字

# 标识符：名字(和C类似)
# 不能以数字开头，不建议以下划线开头(原因和C类似)
# 可以含中文
我草nb233 = 1

# 标识符约定俗成的规则
# 模块：小写开头，_连接多个单词(不能用.)
# 包名：小写开头，.连接多个单词
# 类名：大写开头，Pascal风格(MyFirstClass)
# 常量：大写字母和_
# 模块内部的类：_ + Pascal风格
# __blabla：类私有
# __blabla__：Python专用标识