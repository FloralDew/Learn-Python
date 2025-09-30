import numpy as np
# np.set_printoptions(linewidth=np.inf) # 打印宽度不限制
# np.set_printoptions(threshold=np.inf) # 不截断输出
import matplotlib.pyplot as plt

img = plt.imread("baidu_logo.png") # 此处四通道均被归一化了
# imread返回一个三维数组. 最高维度是高, 次高维度是宽, 最低维[R, G, B]等, 取决于色彩空间
# 此.png图像最低维有四个值: RGBA. A为Alpha, 代表不透明度

## 以下将RGBA转化为RGB, 指定背景为白色, 根据透明度进行混色
rgb_only = img[:, :, :3].copy().astype(np.float32)  # 直接舍弃Alpha通道

# 提取Alpha通道（第四个通道）
alpha_channel = img[:, :, 3]

# 如果你想将RGBA转换为RGB并处理透明度（例如，叠加到白色背景上）
# 定义背景色（这里为白色）
background = np.array([1, 1, 1], dtype=np.float32) 

# 为了与RGB进行运算，需要增加一个维度
alpha_expanded = np.expand_dims(alpha_channel, axis=-1) # axis=-1代表沿最后一个维度

# 计算合成后的RGB：前景色 * alpha + 背景色 * (1 - alpha)
rgb_composited = rgb_only * alpha_expanded + background * (1 - alpha_expanded)

## 以下将rgb转化为灰度图像
cvt = np.array([0.299, 0.587, 0.114], dtype=np.float64)
gray_img = np.dot(rgb_composited, cvt)

plt.figure(figsize=(10, 5))

plt.subplot(121) # 选择子图: 行/列/序号
plt.axis('off') # 隐藏坐标轴
plt.title('rgba -> rgb')
plt.imshow(rgb_composited)

plt.subplot(122)
plt.axis('off')
plt.title('rgb -> gray')
plt.imshow(gray_img, cmap='gray')
# plt.show() # 与Jupyter Notebook不同, 必须show才能看到图像

# pandas读取excel非常方便
import pandas as pd

df = pd.read_excel('Production.xlsx') # 可指定sheet_name
# print(df)

# 解决plt的中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(10, 6))
labels = df['城市']
y = df['9.30']
# print(labels)

# 绘制饼图
plt.pie(y, labels=labels, autopct='%1.1f%%', startangle=90) 
# 倒数第二个参数表示保留一位小数; 最后一个参数使得从坐标系90°开始绘制
# 设置x, y轴刻度
plt.axis('equal') # 正圆
plt.title('Production')
plt.show()