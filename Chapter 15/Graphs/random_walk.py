
from random import choice
class RandomWalk:
# A class to generate random walks.

    def __init__(self, num_points=5000):
    # Initialize attributes of a walk.
        self.num_points = num_points
        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
    # Calculate all the points in the walk

        # loop- keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            # returns either 1 for right movement or −1 for left
            x_direction = choice([1, -1])
            # distance randomly selected between 0 and 4
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            # returns either 1 for up movement or −1 for down
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculates the new position by adding it to the previous value
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            # append new position to list
            self.x_values.append(x)
            self.y_values.append(y)
