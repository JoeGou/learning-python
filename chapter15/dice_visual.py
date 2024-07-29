import plotly.express as px

from die import Die

die1 = Die()
die2 = Die(10)

#投掷几次骰子并将结果存储在一个列表中
results =[]
for roll_num in range(100):
    result1 = die1.roll()
    result2 = die2.roll()
    results.append(result1 + result2)

#分析结果
frequencies = []
poss_results = range(1, die1.num_sides + die2.num_sides +1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

#对结果进行可视化
title = 'Results of rolling one D6 1,000 times'
labels = {'x': 'Result',
        'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y =frequencies, title = title, labels = labels)
fig.update_layout(xaxis_dtick = 3)
fig.show()
fig.write_html('test.html')