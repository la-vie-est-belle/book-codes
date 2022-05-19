from openpyxl import Workbook

# 创建文件对象
wb = Workbook()

# 获取当前正使用的工作表
ws = wb.active

# 添加一些字段
ws.append(['test1', 'test2', 'test3'])

# 保存为test.xlsx
wb.save('test.xlsx')