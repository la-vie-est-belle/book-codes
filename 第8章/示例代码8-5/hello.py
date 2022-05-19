import os

data_path = './data.txt'
with open(data_path, 'r') as f:
    print(f.read())

os.system('pause')  # 暂停程序，好看清输出内容