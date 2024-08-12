from pathlib import Path
from datetime import datetime
import csv
import matplotlib.pyplot as plt

path = Path('weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, row in enumerate(header_row):
    print(index, row)

prcps = []
dates = []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        prcp = float(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        prcps.append(prcp)
        dates.append(current_date)

fig, ax = plt.subplots()
ax.plot(dates, prcps, color = 'blue', linewidth = 1.5)
ax.set_title("sitaka Daily precipitation", fontsize = 16)
ax.set_xlabel("", fontsize =16)
ax.set_ylabel("ml", fontsize =16)
ax.tick_params(labelsize =16)
fig.autofmt_xdate()

plt.show()