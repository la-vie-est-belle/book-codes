import sys
import zipfile


# 解压data.txt到当前路径下
pic_zip = zipfile.ZipFile('data.zip')
pic_zip.extractall('.')
