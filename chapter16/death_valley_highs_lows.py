import matplotlib.pyplot as plt
from datetime import datetime
from pathlib import Path
import csv

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

highs = []
lows = []
dates = []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for{current_date}")
    else:
        highs.append(high)
        lows.append(low)
        dates.append(current_date)

# print(dates)


fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', linewidth = 3, alpha=0.5)
ax.plot(dates, lows, color = 'blue', linewidth = 3, alpha=0.5)
ax.set_title("Daily high-low temperature", fontsize =24)
ax.set_xlabel("", fontsize=16)
ax.set_ylabel("Temperatue(F)", fontsize=16)
ax.tick_params(labelsize =16)
fig.autofmt_xdate()
plt.show()