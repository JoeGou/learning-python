import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c= y_values,  s=10, cmap=plt.cm.spring_r)

#设置图题并给坐标轴加上标签
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.axis([0, 1100, 0, 1_100_000])

#设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()
#plt.savefig('test')