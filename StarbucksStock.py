import csv
import requests
import bs4
from decimal import Decimal
from Algorithm import *

#STORING DATA FROM CSV FILES
StarbucksDates = []
StarbucksPrices = []

count = 0

with open('stockInfo/FB.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            StarbucksDates.append(row[0])
            StarbucksPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count = 1



#SCRAPING FOR CURRENT PRICE

res = requests.get('https://finance.yahoo.com/quote/SBUX?p=SBUX')

soup = bs4.BeautifulSoup(res.text, 'lxml')
StarbucksCurrentPrice = soup.select("span[data-reactid*='21']")[0].text




##SIMPLE MOVING AVERAGE

StarbucksDailyDates = []
StarbucksDailyPrices = []

count1 = 0

with open('stockInfo/FullYearDailyFBData.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count1 == 1:
            StarbucksDailyDates.append(row[0])
            StarbucksDailyPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count1 = 1




##13 DAY MOVING AVERAGE
starbucks_moving_averages13 = []

for i in range(13, len(StarbucksDailyPrices)+1):
    new13 = StarbucksDailyPrices[(i-13) : (i)]
    starbucks_moving_averages13.append(round((sum(new13))/(13.0),2))




##52 DAY MOVING AVERAGE
starbucks_moving_averages52 = []

for i in range(52, len(StarbucksDailyPrices)+1):
    new52 = StarbucksDailyPrices[(i-52) : (i)]
    starbucks_moving_averages52.append(round((sum(new52))/(52.0),2))



#NEXT YEAR ESTIMATE

soup1 = bs4.BeautifulSoup(res.text, 'lxml')
starbucks_nextyearest = soup1.select("span[data-reactid*='90']")[0].text




#RETURN ON ASSETS
res1 = requests.get('https://finance.yahoo.com/quote/SBUX/key-statistics?p=SBUX')

soup2 = bs4.BeautifulSoup(res1.text, 'lxml')
starbucks_returnassets = soup2.select("td[data-reactid*='133']")[0].text


#VOLUME

soup3 = bs4.BeautifulSoup(res.text, 'lxml')
starbucks_volume = soup1.select("span[data-reactid*='41']")[0].text