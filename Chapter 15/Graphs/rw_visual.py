import matplotlib.pyplot as plt

#from Graphs.random_walk import RandomWalk
from random_walk import *

# Keep making new walks, as long as the program is active.
while True:

    # create a random walk
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # plot the points in the walk
    plt.style.use('classic')
    #fig, ax = plt.subplots(figsize=(15, 9))
    #fig, ax = plt.subplots()
    fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

    # set point_numbers to num_points to the RandomWalk class
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)

    # this feeds the walks x and y values to scatter() with size=15
    #ax.scatter(rw.x_values, rw.y_values, s=15)

    # Emphasize the first and last points.
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break