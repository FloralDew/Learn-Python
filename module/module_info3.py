if __name__ == '__main__': # 只有直接运行时会执行, 在作为模块被导入时不会执行
    print("this is module_info3")
    
name = 'Gary'
age = 90

def info():
    print(f'Name: {name}, Age: {age}')