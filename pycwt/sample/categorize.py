import numpy
import pandas as pd

#分类，读取txt文件，按width数值进行分类并保存为4个txt文件
xiaoyu20 = []
to119 = []
to359 = []
is360 = []
with open(r'D:\wwh\小波光谱分析\pycwt\cdaw.gsfc.nasa.gov\CME_list\UNIVERSAL_ver2\text_ver\univ_all.txt', 'r') as file:
    a = 1
    for line in file:
        if a <= 4:
            a+=1
            continue
        width = int(line.split()[3])
        if width <= 20:
            xiaoyu20.append(line)
        elif width <= 119:
            to119.append(line)
        elif width <= 359:
            to359.append(line)
        else:
            is360.append(line)

with open('19.txt', 'w') as file:
    for line in xiaoyu20:
        file.write(line)
with open('119.txt', 'w') as file:
    for line in to119:
        file.write(line)
with open('359.txt', 'w') as file:
    for line in to359:
        file.write(line)
with open('360.txt', 'w') as file:
    for line in is360:
        file.write(line)
