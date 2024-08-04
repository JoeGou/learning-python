from pathlib import Path
import json
import plotly.express as px
import pandas as pd

#将数据作为字符串读取并转为python对象
path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#将数据文件转为更易阅读的版本
path = Path('eq_data/readable_all_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags = []
titles =[]
lons = []
lats = []


for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)


# print(mags[:5])
# print(titles[:5])
# print(lons[:5])
# print(lats[:5])
data = pd.DataFrame(data=zip(lons, lats, titles, mags), columns=['经度','纬度','位置','震级'])
# print(data.head())
title = "global_earthquakes"
labels = {'x': 'lons', 'y': 'lats'}
# fig = px.scatter(x=lons, y=lats, title = title, labels = labels)
fig = px.scatter(data, x='经度', y='纬度', size = '震级',size_max=10, color = '震级', color_continuous_scale='mygbm', title = title, labels = labels)

fig.show()
