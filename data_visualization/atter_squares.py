import matplotlib.pyplot as plt

x_values = range(1, 101)
y_values = [x ** 2 for x in x_values]
"""使用scatter绘制散点图"""
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values,c='green', s=10)
# ax.scatter(x_values, y_values,c=(0,0.8,0), s=10)
# 颜色映射
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# 设置图表标题并给坐标轴加上标签ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', which='major', labelsize=14)

# 设置坐标轴的取值范围
ax.axis([0, 110, 0, 11000])

# plt.show()
# 将图标自动保存到文件中
# 第一个实参指定以什么文件保存图表，这个文件将存储到atter_squares.py所在的目录中
# 第二个实参指定将图表多余的空白区域裁剪掉
plt.savefig('aquares_plot.png', bbox_inches='tight')
