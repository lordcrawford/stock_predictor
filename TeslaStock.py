import csv
import requests
import bs4
from decimal import Decimal


#STORING DATA FROM CSV FILES
TeslaDates = []
TeslaPrices = []

count = 0

with open('stockInfo/TSLA.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count == 1:
            TeslaDates.append(row[0])
            TeslaPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count = 1



#SCRAPING FOR CURRENT PRICE

res = requests.get('https://finance.yahoo.com/quote/TSLA?p=TSLA')

soup = bs4.BeautifulSoup(res.text, 'lxml')
TeslaCurrentPrice = soup.select("span[data-reactid*='21']")[0].text




##SIMPLE MOVING AVERAGE

TeslaDailyDates = []
TeslaDailyPrices = []

count1 = 0

with open('stockInfo/FullYearDailyTeslaData.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        if count1 == 1:
            TeslaDailyDates.append(row[0])
            TeslaDailyPrices.append(float(round(Decimal(row[1]), 2)))
        else:
            count1 = 1




##13 DAY MOVING AVERAGE
tesla_moving_averages13 = []

for i in range(13, len(TeslaDailyPrices)+1):
    new13 = TeslaDailyPrices[(i-13) : (i)]
    tesla_moving_averages13.append(round((sum(new13))/(13.0),2))




##52 DAY MOVING AVERAGE
tesla_moving_averages52 = []

for i in range(52, len(TeslaDailyPrices)+1):
    new52 = TeslaDailyPrices[(i-52) : (i)]
    tesla_moving_averages52.append(round((sum(new52))/(52.0),2))