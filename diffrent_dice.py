from die import Die
import pygal

#创建一个D6和D10
die_1 = Die(6)
die_2 = Die(10)

#掷色子多次
results = []
for roll_num in range(50000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
#可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling a D6 and a D10 50000 times."

hist.x_labels = [x for x in range(2,max_result+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Result"

hist.add('D6+D10',frequencies)
hist.render_to_file('dice2_visual.svg')