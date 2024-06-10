import numpy as np

# 创建一个NumPy数组
# array = np.array([[1, 2, 3], [4, 5, 6]])
# date = [str(l.split()[0]) for l in open("univ_all.txt")]
# array = np.array(date)
# print(1234)

# # 将数组保存到.npy文件
# np.save('np_all.npy', array)
data = np.load('Partial Halo CME Low50_x.npy',allow_pickle=True)
print(data)