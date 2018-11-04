from die import Die

die = Die(6)
#掷几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)