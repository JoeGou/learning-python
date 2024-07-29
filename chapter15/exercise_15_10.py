import matplotlib.pyplot as plt
import plotly.express as px

from die import Die

die1 = Die()
die2 = Die()
die3 = Die()

#投掷几次骰子并将结果存储在一个列表中
results =[]
for roll_num in range(1001):
    result1 = die1.roll()
    result2 = die2.roll()
    result3 = die3.roll()
    results.append(result1 * result2 * result3)

#分析结果

poss_results = range(1, die1.num_sides ** 3 +1)
frequencies = [results.count(x) for x in poss_results]
# for value in poss_results:
#     frequency = results.count(value)
#     frequencies.append(frequency)

#对结果进行可视化
title = 'Results of rolling three D6 1,000 times'
labels = {'x': 'Result',
        'y': 'Frequency of Result'}
fig, ax = plt.subplots(figsize=(15, 9))
ax.scatter(poss_results, frequencies)
plt.show()
# fig.write_html('test.html')