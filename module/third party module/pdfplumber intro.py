# 从pdf文件中提取数据
import pdfplumber

# 打开pdf文件
with pdfplumber.open("Application.pdf") as pdf:
    for i in pdf.pages: # 遍历每个页
        print(i.extract_text()) # 提取内容
        print(f'Page {i.page_number}'.center(60, '-'))