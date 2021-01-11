from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create two dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []

# rolls the dice 50k times & stores results in a list named results
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


# Analyze the results
# Creating an empty list to store the frequency for each value in results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for loop to iterate results & count the frequency for each value
for value in range(2, max_result+1):
    frequency = results.count(value)
    # Appends the frequency to the frequencies list
    frequencies.append(frequency)

# Visualize the results

# results stores in list called x_values, starting a 2 to # of sides on die
x_values = list(range(2, max_result+1))

# The Plotly class Bar() represents a data set that will be formatted as a bar chart
data = [Bar(x=x_values, y=frequencies)]

# sets title to each axis in graph
# dtick = distance between ticks
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

# graph title & pass the x- and y-axis configuration dictionaries as well
my_layout = Layout(title='Results of rolling a D6 and a D10 50000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# generate the plot, we call the offline.plot() function
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')



print(frequencies)
