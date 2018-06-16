#import matplotlib.pyplot as plt
import csv
import requests
import bs4

AppleDates = []
ApplePrices = []

count = 0

with open('stockInfo/AAPL (1).csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            AppleDates.append(row[0])
            ApplePrices.append(int(float(row[1])))
        else:
            count = 1



res = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL')

soup = bs4.BeautifulSoup(res.text, 'lxml')
AppleCurrentPrice = soup.select("span[data-reactid*='21']")[0].text


"""

    look up tkinter to make application nicer*******
    
    do the function for simple moving averages and exponential averages *******
        for example like def movingaverage(dataset,window)
        window is number of days
        alice will tell me intervals
    
    add a utility for adding moving average lines on the graphs  *********
    fix y-axis grid
    
    make the pages scrollable or the algorithm data could pop up in a window where you have to input data
    
    
    add something that will move along the graphs and display data (having a side box that will display other information for that data value)
    
    
    
    
    ask alice for the other stocks, so far Apple i have (maybe Google, Amazon, Facebook, Tesla)
    
    
    
    customize home page to show whether stocks are good buys or not, will get this data from yahoo finance (having a nice table layout) ********
        and find background image or color
    
    
    
    
    
    
    
    WORK ON ALGORITHM AFTER THAT*****
    
    -can use the esg score to help
    
    
"""


"""
plt.figure(figsize=(12,8.5))
plt.plot(dates,prices, label='Market Prices')
plt.xlabel('Dates')
plt.xticks(rotation=90)
plt.ylabel('Prices')
plt.title('Apple Stock')
plt.legend()
plt.show()
"""
