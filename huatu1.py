import matplotlib.pyplot as plt
x_one_values=list(range(1,5001))
y_one_values=[x**3 for x in x_one_values]
color_one='green'
plt.scatter(x_one_values,y_one_values,c=y_one_values,cmap=plt.cm.Blues,edgecolor='none',s=40)
plt.show()