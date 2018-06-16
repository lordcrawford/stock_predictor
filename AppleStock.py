#import matplotlib.pyplot as plt
import csv
import requests
import bs4
from decimal import Decimal



#STORING DATA FROM CSV FILES
AppleDates = []
ApplePrices = []

count = 0

with open('stockInfo/AAPL (1).csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            AppleDates.append(row[0])
            ApplePrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count = 1




#SCRAPING FOR CURRENT PRICE
res = requests.get('https://finance.yahoo.com/quote/AAPL?p=AAPL')

soup = bs4.BeautifulSoup(res.text, 'lxml')
AppleCurrentPrice = soup.select("span[data-reactid*='21']")[0].text




##SIMPLE MOVING AVERAGE

AppleDailyDates = []
AppleDailyPrices = []

count1 = 0

with open('stockInfo/FullYearDailyAppleData.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count1 == 1:
            AppleDailyDates.append(row[0])
            AppleDailyPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count1 = 1




##13 DAY MOVING AVERAGE
apple_moving_averages13 = []

for i in range(13, len(AppleDailyPrices)+1):
    new13 = AppleDailyPrices[(i-13) : (i)]
    apple_moving_averages13.append(round((sum(new13))/(13.0),2))




##52 DAY MOVING AVERAGE
apple_moving_averages52 = []

for i in range(52, len(AppleDailyPrices)+1):
    new52 = AppleDailyPrices[(i-52) : (i)]
    apple_moving_averages52.append(round((sum(new52))/(52.0),2))





"""

    look up tkinter to make application nicer*******
    
    
    
    make the pages scrollable or the algorithm data could pop up in a window where you have to input data
    
    
    add something that will move along the graphs and display data (having a side box that will display other information for that data value)
    
    
    
    
    
    
    
    customize home page to show whether stocks are good buys or not, will get this data from yahoo finance (having a nice table layout) ********
        and find background image or color
    
    
    
    
    
    
    
    WORK ON ALGORITHM AFTER THAT*****
    
    -can use the esg score to help
    use line of best fit
    
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
