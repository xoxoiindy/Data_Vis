from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# Create one D6 dice.
die = Die()


# Make some rolls, and store results in a list.
results = []

# rolls the dice 1000x & stores results in a list named results
for roll_num in range(1000):
    result = die.roll()
    results.append(result)


# Analyze the results
# Creating an empty list to store the frequency for each value in results
frequencies = []
# for loop to iterate results & count the frequency for each value
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    # Appends the frequency to the frequencies list
    frequencies.append(frequency)

# Visualize the results

# results stores in list called x_values, starting a 1 to # of sides on die
x_values = list(range(1, die.num_sides+1))

# The Plotly class Bar() represents a data set that will be formatted as a bar chart
data = [Bar(x=x_values, y=frequencies)]

# sets title to each axis in graph
x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}

# graph title & pass the x- and y-axis configuration dictionaries as well
my_layout = Layout(title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)

# generate the plot, we call the offline.plot() function
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')



print(frequencies)
print(results)
print(x_values)

