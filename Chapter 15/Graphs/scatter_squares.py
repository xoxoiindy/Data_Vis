import matplotlib.pyplot as plt

# x-values containing 1 -1000
x_values = range(1, 1001)
# y-values loop through the x-values
y_values = [x**2 for x in x_values]

#style import from matplotlib
plt.style.use('seaborn')

fig, ax = plt.subplots()
# cmap (colormap) argument - lower y-values light blue - higher y-values dark blue
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# scatter() uses the s argument to set the size of the dots used to draw the graph
#ax.scatter(2, 4)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# automatically saves plot file - second argument trims extra whitespace
# plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()

