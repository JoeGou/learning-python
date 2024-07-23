import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #创建一个Randomwalk实例
    rw = RandomWalk()
    rw.fill_wwalk()

    #将所有的点绘制出来
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')
    plt.show()
    
    if input("Make another walk? (y/n) ") == 'n':
        break