import matplotlib.pyplot as plt
import csv

dates = []
prices = []

count = 0

with open('/Users/lordcrawford/Desktop/AAPL (1).csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            dates.append(row[0])
            prices.append(int(float(row[1])))
        else:
            count = 1



plt.figure(figsize=(12,8.5))
plt.plot(dates,prices, label='Loaded from file!')
plt.xlabel('dates')
plt.xticks(rotation=90)
plt.ylabel('prices')
plt.title('Apple Stock')
plt.legend()
plt.show()