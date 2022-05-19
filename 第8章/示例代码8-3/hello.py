import tkinter
import sys
import os


def res_path(relative_path):		# 1
    """获取资源路径"""
    try:
        # 获取_MEI文件夹所在路径
        base_path = sys._MEIPASS
    except Exception:
        # 没有_MEI文件夹的话使用当前路径
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


win = tkinter.Tk()
win.iconbitmap(res_path('./icon.ico'))  # 设置窗口图标
win.mainloop()