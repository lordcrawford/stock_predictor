from math import *

#Gives you location of intersections and if you use the length function you can find number of intersections

def intersection(shortavg,longavg,dates):
    intersections = []

    a = 39

    for i in range(52,len(longavg)-1):
        if(a<239):
            if(abs(shortavg[a] - longavg[i]) < .1):
                intersections.append(dates[i])
        a = a + 1

    return(intersections)






def standard_deviation(list):
    """Calculates the standard deviation for a list of numbers."""
    num_items = len(list)
    mean = sum(list) / num_items
    differences = [x - mean for x in list]
    sq_differences = [d ** 2 for d in differences]
    ssd = sum(sq_differences)


    variance = ssd / num_items

    sd = sqrt(variance)

    return sd







def buyingstrategy(intersections, prices, dates, shortavg, longavg):
    shares = 0
    money = 100000
    buy = True

    firstindex = dates.index(intersections[0])

    if(shortavg[firstindex - 13] < longavg[firstindex - 52]):
        buy = True


    for i in range(1, 8):

        a = intersections[i]
        b = dates.index(a)

        currentprice = prices[b]

        if (buy):
            if(money > 0 ):
                shares = money / currentprice
                money = 0

        if(buy == False):
            if(shares>0):
                money = shares * currentprice
                shares = 0

        buy = not buy


    if(money == 0):
        money = shares * currentprice

    return round(money,2)

"""
LINEAR REGRESSION MODEL

from sklearn.linear_model import LinearRegression

    def linear_regression_model(x,y):
        model = LinearRegression(fit_intercept=True)

        model.fit(x[:, np.newaxis], y)
        
        xfit = np.linspace(0, 10, 1000)
        yfit = model.predict(xfit[:, np.newaxis])
        
        plt.scatter(x, y)
        plt.plot(xfit, yfit);
        
        
        
    
    x is the prices
    y is the dates
"""



