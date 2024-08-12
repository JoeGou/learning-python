from pathlib import Path
from datetime import datetime
import csv

import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)
# print(next(reader)[2])
# for index, column_header in enumerate(header_row):
#     print(index, column_header)


#提取最高温度
highs = []
datatimes = []
for row in reader:
    high = int(row[4])
    datatime = row[2]
    highs.append(high)
    datatimes.append(datatime)

print(len(datatimes))
print(len(highs))

#根据最高温度绘图
plt.style.use('seaborn-v0_8-talk')

fig, ax = plt.subplots(figsize=(15,9))
x_values = list(range(0,len(highs)))
plt.plot(datatimes, highs, linewidth= 3, color = 'red', )
# print(x_values)
# plt.scatter(datatime, highs, s=10)
ax.set_title('sitaka Daily high temperature')
ax.set_xlabel('', fontsize = 10)
ax.set_ylabel('Temperatue (F)', fontsize = 10)


plt.show()