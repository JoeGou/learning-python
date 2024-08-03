import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import csv

path1 = Path('weather_data/death_valley_2021_simple.csv')
lines1 = path1.read_text().splitlines()

path2 = Path('weather_data/sitka_weather_2021_simple.csv')
lines2 = path2.read_text().splitlines()

reader1 = csv.reader(lines1)
header_row1 = next(reader1)

reader2 = csv.reader(lines2)
header_row2 = next(reader2)
# print(header_row1)

# for index, column_header in enumerate(header_row1):
#     print(index, column_header)

highs1 = []
lows1 = []
dates1 = []
for row in reader1:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for death_valley {current_date}")
    else:
        highs1.append(high)
        lows1.append(low)
        dates1.append(current_date)

highs2 = []
lows2 = []
dates2 = []
for row in reader2:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for sitaka{current_date}")
    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(current_date)

# print(dates)


fig, ax = plt.subplots()
ax.plot(dates1, highs1, color = 'red', linewidth = 3, alpha=0.5)
ax.plot(dates1, lows1, color = 'blue', linewidth = 3, alpha=0.5)
ax.plot(dates2, highs2, color = 'green', linewidth = 3, alpha=0.5)
ax.plot(dates2, lows2, color = 'yellow', linewidth = 3, alpha=0.5)
ax.set_title("Daily high-low temperature", fontsize =24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperatue(F)", fontsize=16)
ax.tick_params(labelsize =16)
fig.autofmt_xdate()
plt.show()