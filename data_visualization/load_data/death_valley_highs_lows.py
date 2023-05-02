import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row):
        print(index,column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Miss data for {current_date}")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)
    # 根据最高、最低温度绘制图形
    plt.style.use('seaborn')
    # 解决中文乱码问题
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    fig,ax =plt.subplots()

    ax.plot(dates,highs,c='red')
    ax.plot(dates,lows,c='blue')
    ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

    # 设置图形的格式
    ax.set_title("2018年每日最高、最低温度", fontsize=14)
    ax.set_xlabel('', fontsize=6)

    # 绘制倾斜的日期标签，以免其彼此重叠
    fig.autofmt_xdate()

    ax.set_ylabel('温度（F）', fontsize=16)
    ax.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
