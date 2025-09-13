# .py文件就是一个模块(特定功能的代码的封装). 模块可以避免变量, 函数名称相冲突的问题
# 模块命名时全部使用小写字母 多个单词用下划线分割
# 若自定义模块名称和系统内置相同, 导入自定义的

## 模块的导入
import module_info # 相当于先执行一遍module_info.py, 因此里面的print也会输出
print(module_info.name) # 注意要先保存module_info.py

import module_info as mi
print(mi.name)

from module_info import name, info # 导入具体变量或函数或类
print(name) # 使用from方式调用, 无需使用模块.
info()

# 使用通配符导入全部
from module_info import *
age()
 
# 同时导入多个模块
import random, time
from math import log, sinh, floor

# 若导入模块中具有同名变量或函数, 后导入的会将之前导入的覆盖
from module_info2 import info # 里面的print也会输出
info()
# 解决此问题: import两个模块, 使用模块.来调用

import module_info3 as mi3 # 此时不会执行print, 因为使用了if __name__
print(mi3.name)