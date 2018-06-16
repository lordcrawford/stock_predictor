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
plt.figure(figsize=(12,8.5))
plt.plot(dates,prices, label='Market Prices')
plt.xlabel('Dates')
plt.xticks(rotation=90)
plt.ylabel('Prices')
plt.title('Apple Stock')
plt.legend()
plt.show()
"""
