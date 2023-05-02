import matplotlib.pyplot as plt

# 输入值
input_values = [1, 2, 3, 4, 5]
# 输出值
squares = [1, 4, 9, 16, 25]
# 使用系统内置的样式
plt.style.use('seaborn')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
# fig表示整张图片
# ax表示图片中的各个图表
fig, ax = plt.subplots()
# 方法plot（）尝试根据给定的数据以有意义的方式绘制图表
ax.plot(input_values, squares, linewidth=3)
# 设置图表标题并给坐标轴加上标签
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
# 打开matplotlib查看器并显示绘制的图表
plt.show()
