import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

#画每日CME次数图

# ways = ['univ_all.txt', '19.txt', '119.txt', '359.txt', '360.txt']
# titles = ['All CME', 'Narrow CME', 'Normal CME', 'Partial Halo CME', 'Halo CME']
# fig, axs = plt.subplots(5, 1, figsize=(10, 10))

ways = ['359_latitude_low50.txt', '359_latitude_high.txt']
titles = ['Partial Halo CME Low50', 'Partial Halo CME High']
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

#ways = ['19_latitude_low50.txt', '19_latitude_high.txt']
#titles = ['Narrow CME Low50', 'Narrow CME High']
# fig, axs = plt.subplots(2, 1, figsize=(10, 10))

#ways = ['119_latitude_low.txt', '119_latitude_high.txt']
#ways = ['119_latitude_low50.txt', '119_latitude_high.txt']
#titles = ['Normal CME Low50', 'Normal CME High']
#fig, axs = plt.subplots(2, 1, figsize=(10, 10))
i = 0
for way in ways:
    dates = []
    with open(way, 'r') as file:
        for line in file:
            parts = line.strip().split()    # 假设日期和其余部分以空格分隔
            date_str = parts[0]
            # 将字符串日期转换为datetime对象
            date = datetime.strptime(date_str, '%Y/%m/%d')  # 假设日期格式为'年-月-日'
            dates.append(date)
    # 统计每个日期出现的次数
    date_counts = Counter(dates)

    # 准备绘制柱状图的数据
    days = list(date_counts.keys())  # 日期列表
    counts = list(date_counts.values())  # 对应的计数列表
    axs[i].bar(days, counts, width = 1.5)
    axs[i].set_title(titles[i])
    axs[i].set_ylabel('Number')
    i += 1

for ax in axs.flat:
    ax.set_xlabel('Time(year)')
plt.tight_layout()  # 调整子图之间的间距
# plt.savefig('The daily occurrence rate of CMEs.png')
# plt.savefig('Partial Halo CME Low and High.png')
plt.savefig('Partial Halo Low50 and High.png')
#plt.savefig('Normal CME Low50 and High.png')
plt.show()

# with open('19.txt', 'r') as file:
#     for line in file:
#         parts = line.strip().split()    # 假设日期和其余部分以空格分隔
#         date_str = parts[0]
#         # 将字符串日期转换为datetime对象
#         date = datetime.strptime(date_str, '%Y/%m/%d')  # 假设日期格式为'年-月-日'
#         dates.append(date)

# # 统计每个日期出现的次数
# date_counts = Counter(dates)

# # 准备绘制柱状图的数据
# days = list(date_counts.keys())  # 日期列表
# counts = list(date_counts.values())  # 对应的计数列表

# # 将日期转换为天数（以便于作为横坐标）
# # days = [(day - datetime(1996, 1, 1)).days for day in days]

# # 绘制柱状图
# plt.figure(figsize=(20, 6))  # 设置图形大小
# plt.bar(days, counts, width=1.5)  # 绘制柱状图，width为柱子的宽度
# plt.yticks(range(0,16,5))

# # 设置横坐标的格式
# # plt.gcf().autofmt_xdate()  # 自动旋转日期标签
# # date_format = plt.DateFormatter('%Y/%m/%d')
# # plt.gca().xaxis.set_major_formatter(date_format)

# # 设置标题和坐标轴标签
# plt.title('Narrow CME')
# plt.xlabel('Date')
# plt.ylabel('Occurrences')

# # 显示图形
# plt.savefig('Narrow CME.png')
# plt.show()
#test