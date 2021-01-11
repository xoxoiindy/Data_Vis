import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'

# open the file and assign the resulting file object to f
with open(filename) as f:
    # call csv.reader() and pass it the f object as an argument to create a reader object associated with that file
    reader = csv.reader(f)
    # calls next() with the first line of the file that which contains the headers
    header_row = next(reader)


    # Get dates and high temperatures from this file.
    # Lists
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# Plot the high & low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2018\nDeath Valley, CA"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()


# enumerate() function returns both the index of each item and the value of each item as you loop through a list
#for index, column_header in enumerate(header_row):

   # print(index, column_header)