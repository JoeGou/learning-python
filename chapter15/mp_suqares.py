import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

input_values_2 = [1, 2, 3, 4, 5]
squares_2 = [1, 4, 9, 16, 25]

plt.style.use('tableau-colorblind10')
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].plot(input_values, squares, linewidth=3)
ax[1].plot(input_values_2, squares_2, linewidth=3)

#设置图题并给坐标轴加上标签
ax[0].set_title("Square numbers", fontsize=24)
ax[0].set_xlabel("Value", fontsize=14)
ax[0].set_ylabel("Square of Value", fontsize=14)

#设置刻度标记的样式
ax[0].tick_params(labelsize=14)
plt.show()