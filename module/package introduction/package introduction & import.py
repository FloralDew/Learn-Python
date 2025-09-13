# 包: 含有__init__.py文件的文件夹, 可以避免模块名称相冲突的问题

import package_admin.module_intro as mi # 包名.模块名
mi.info() # __init__文件中的代码自动先被执行

# 方法2
from package_admin import module_intro as mi # 第二次导入不会执行__init__
print(mi.name)

from package_admin.module_intro import *
print(name)