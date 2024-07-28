import plotly.express as px

from die import Die

die = Die()

#投掷几次骰子并将结果存储在一个列表中
results =[]
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
title = 'Results of rolling one D6 1,000 times'
labels = {'x': 'Result',
        'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y =frequencies, title = title, labels = labels)
fig.show()