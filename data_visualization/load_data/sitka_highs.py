import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reder = csv.reader(f)
    header_row = next(reder)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)
    # 从文件中获取最高温度
    dates,lows,highs =[], [],[]
    for row in reder:
        current_date=datetime.strptime(row[2],'%Y-%m-%d')
        low=int(row[6])
        high = int(row[5])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)

# 根据最高温度绘图形
plt.style.use('seaborn')
# 解决中文乱码问题
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

fig, ax = plt.subplots()
ax.plot(dates,highs,c='red',alpha=0.5)
ax.plot(dates,lows,c='blue',alpha=0.5)

ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)
# 设置坐标轴的范围
# ax.axis([0,len(highs),50,80])

# 设置图形的格式
ax.set_title("2018年每日最高、最低温度", fontsize=24)
ax.set_xlabel('', fontsize=16)

#绘制倾斜的日期标签，以免其彼此重叠
fig.autofmt_xdate()

ax.set_ylabel('温度（F）', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()
