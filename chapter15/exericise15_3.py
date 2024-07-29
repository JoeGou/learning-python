import matplotlib.pyplot as plt

from random_walk import RandomWalk


#创建一个Randomwalk实例
rw = RandomWalk()
rw.fill_wwalk()

#将所有的点绘制出来
plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9))
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolors='none', cmap=plt.cm.Blues, s=1)
ax.set_aspect('equal')

#突出起点和终点
ax.scatter(0, 0, c="green", edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',  s=100)

#隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
    

