import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *

from PIL import Image, ImageTk





from AppleStock import AppleDates,ApplePrices, AppleCurrentPrice, \
    AppleDailyPrices, AppleDailyDates, apple_moving_averages13, apple_moving_averages52, apple_nextyearest, apple_returnassets, apple_volume

from AmazonStock import AmazonDates, AmazonPrices, AmazonDailyDates,\
    AmazonDailyPrices, AmazonCurrentPrice, amazon_moving_averages13, amazon_moving_averages52, amazon_nextyearest, amazon_returnassets, amazon_volume

from TeslaStock import TeslaDates, TeslaPrices, TeslaDailyDates,\
    TeslaDailyPrices, TeslaCurrentPrice, tesla_moving_averages13, tesla_moving_averages52, tesla_nextyearest, tesla_returnassets, tesla_volume

from FacebookStock import FacebookDates, FacebookPrices, FacebookDailyDates,\
    FacebookDailyPrices, FacebookCurrentPrice, facebook_moving_averages13, facebook_moving_averages52, facebook_nextyearest, facebook_returnassets, facebook_volume

from Algorithm import intersection, buyingstrategy






LARGE_FONT = ("Verdana", 12)
FONT = ("Verdana", 30)
font = ("Verdana", 16)
style.use("ggplot")




class StockAnalysis(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self,"Stock Predictor")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (InitialPage, AmazonStock, TeslaStock, AppleStock, FacebookStock, StockIndicators):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky = "nsew")


        self.show_frame(InitialPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()





class InitialPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text = "Stock Predictor", font=FONT, )
        label.pack(pady=60)

        button1 = ttk.Button(self, text="Apple Stock", command=lambda: controller.show_frame(AppleStock))
        button1.pack(pady=25)

        load = Image.open('pictures/stock.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=60,y=65)

        load2 = Image.open('pictures/stock1.png')
        render2 = ImageTk.PhotoImage(load2)

        img2 = Label(self, image=render2)
        img2.image = render2
        img2.place(x=850, y=0)

        load3 = Image.open('pictures/background.png')
        render3 = ImageTk.PhotoImage(load3)

        img3 = Label(self, image=render3)
        img3.image = render3
        img3.place(x=130, y=528)




        button2 = ttk.Button(self, text = "Amazon Stock", command=lambda: controller.show_frame(AmazonStock))
        button2.pack(pady=25)

        button4 = ttk.Button(self, text="Facebook Stock", command=lambda: controller.show_frame(FacebookStock))
        button4.pack(pady=25)

        button3 = ttk.Button(self, text="Tesla Stock", command=lambda: controller.show_frame(TeslaStock))
        button3.pack(pady=25)

        button5 = ttk.Button(self, text="Stock Indicators", command=lambda: controller.show_frame(StockIndicators))
        button5.pack(pady=25)










class AppleStock(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Apple Stock (Graph)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(InitialPage))
        button1.pack()




        #GRAPHSSSSSSS


        f = Figure(figsize=(14,8), dpi=100)
        ax = f.add_subplot(111, label = "1")
        ax2 = f.add_subplot(111, label = "2",frame_on=False)
        ax3 = f.add_subplot(111, label = "3",frame_on=False)

        title = "Apple Stock Prices\nCurennt Price: " + AppleCurrentPrice


        #REGULAR PRICE LINE
        ax.plot(AppleDates,ApplePrices, 'b', label = "Stock Price",linewidth=2)
        ax.set_title(title)
        ax.tick_params('x', labelrotation=90)
        ax.set_ylim([140, 200])



        #13 DAY MOVING AVERAGE LINE
        ax2.plot(AppleDailyDates[12:], apple_moving_averages13, 'g--', label = "13 Day Moving Average")
        ax2.axes.get_xaxis().set_visible(False)
        ax2.set_ylim([140, 200])




        #52 DAY MOVING AVERAGE LINE
        ax3.plot(AppleDailyDates[51:], apple_moving_averages52, 'r--', label = "52 Day Moving Average")
        ax3.axes.get_xaxis().set_visible(False)
        ax3.set_ylim([140, 200])






        f.legend()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand = True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand = True)



        #ALGORITHM

        intersections = intersection(apple_moving_averages13,apple_moving_averages52,AppleDailyDates)

        moneymade = buyingstrategy(intersections, AppleDailyPrices, AppleDailyDates, apple_moving_averages13, apple_moving_averages52)

        #ALGORITHM FINDINGS
        def clicked():
            messagebox.showinfo('Algorithm Findings', 'Crossing Average Intersections: ' + str(len(intersections)) + '\n' 
                                "Intersection Dates: " + '\n' + str(intersections) + '\n' + 'Start Money: 100000.00 ' + '\n'
                                + 'End Money: ' + str(moneymade))


        button2 = ttk.Button(self, text="Algorithm Findings", command=clicked)
        button2.pack()









class AmazonStock(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Amazon Stock (Graph)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(InitialPage))
        button1.pack()



        #GRAPHSSSS


        f = Figure(figsize=(14, 8), dpi=100)
        ax = f.add_subplot(111, label="1")
        ax2 = f.add_subplot(111, label="2", frame_on=False)
        ax3 = f.add_subplot(111, label="3", frame_on=False)

        title = "Amazon Stock Prices\nCurennt Price: " + AmazonCurrentPrice

        # REGULAR PRICE LINE
        ax.plot(AmazonDates, AmazonPrices, 'b', label="Stock Price",linewidth=2)
        ax.set_title(title)
        ax.tick_params('x', labelrotation=90)
        ax.set_ylim([900, 1800])

        # 13 DAY MOVING AVERAGE LINE
        ax2.plot(AppleDailyDates[12:], amazon_moving_averages13, 'g--', label="13 Day Moving Average")
        ax2.axes.get_xaxis().set_visible(False)
        ax2.set_ylim([900, 1800])

        # 52 DAY MOVING AVERAGE LINE
        ax3.plot(AmazonDailyDates[51:], amazon_moving_averages52, 'r--', label="52 Day Moving Average")
        ax3.axes.get_xaxis().set_visible(False)
        ax3.set_ylim([900, 1800])




        f.legend()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



        
        #ALGORITHM

        intersections = intersection(amazon_moving_averages13,amazon_moving_averages52,AmazonDailyDates)


        #ALGORITHM FINDINGS
        def clicked():
            messagebox.showinfo('Algorithm Findings', 'Crossing Average Intersections: ' + str(len(intersections)) + '\n' 
                                "Intersection Dates: " + '\n' + str(intersections))


        button2 = ttk.Button(self, text="Algorithm Findings", command=clicked)
        button2.pack()











class TeslaStock(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Tesla Stock (Graph)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(InitialPage))
        button1.pack()

        # GRAPHSSSS

        f = Figure(figsize=(14, 8), dpi=100)
        ax = f.add_subplot(111, label="1")
        ax2 = f.add_subplot(111, label="2", frame_on=False)
        ax3 = f.add_subplot(111, label="3", frame_on=False)



        title = "Tesla Stock Prices\nCurennt Price: " + TeslaCurrentPrice



        # REGULAR PRICE LINE
        ax.plot(TeslaDates, TeslaPrices, 'b', label="Stock Price",linewidth=2)
        ax.set_title(title)
        ax.tick_params('x', labelrotation=90)
        ax.set_ylim([225, 400])

        # 13 DAY MOVING AVERAGE LINE
        ax2.plot(TeslaDailyDates[12:], tesla_moving_averages13, 'g--', label="13 Day Moving Average")
        ax2.axes.get_xaxis().set_visible(False)
        ax2.set_ylim([225, 400])

        # 52 DAY MOVING AVERAGE LINE
        ax3.plot(TeslaDailyDates[51:], tesla_moving_averages52, 'r--', label="52 Day Moving Average")
        ax3.axes.get_xaxis().set_visible(False)
        ax3.set_ylim([225, 400])

        f.legend()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



        #ALGORITHM

        intersections = intersection(tesla_moving_averages13,tesla_moving_averages52,TeslaDailyDates)



        #ALGORITHM FINDINGS
        def clicked():
            messagebox.showinfo('Algorithm Findings', 'Crossing Average Intersections: ' + str(len(intersections)) + '\n' 
                                "Intersection Dates: " + '\n' + str(intersections) )


        button2 = ttk.Button(self, text="Algorithm Findings", command=clicked)
        button2.pack()








class FacebookStock(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Facebook Stock (Graph)", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(InitialPage))
        button1.pack()

        # GRAPHSSSS

        f = Figure(figsize=(14, 8), dpi=100)
        ax = f.add_subplot(111, label="1")
        ax2 = f.add_subplot(111, label="2", frame_on=False)
        ax3 = f.add_subplot(111, label="3", frame_on=False)

        title = "Facebook Stock Prices\nCurennt Price: " + FacebookCurrentPrice

        # REGULAR PRICE LINE
        ax.plot(FacebookDates, FacebookPrices, 'b', label="Stock Price", linewidth=2)
        ax.set_title(title)
        ax.tick_params('x', labelrotation=90)
        ax.set_ylim([140, 205])

        # 13 DAY MOVING AVERAGE LINE
        ax2.plot(FacebookDailyDates[12:], facebook_moving_averages13, 'g--', label="13 Day Moving Average")
        ax2.axes.get_xaxis().set_visible(False)
        ax2.set_ylim([140, 205])

        # 52 DAY MOVING AVERAGE LINE
        ax3.plot(FacebookDailyDates[51:], facebook_moving_averages52, 'r--', label="52 Day Moving Average")
        ax3.axes.get_xaxis().set_visible(False)
        ax3.set_ylim([140, 205])

        f.legend()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # ALGORITHM

        intersections = intersection(facebook_moving_averages13, facebook_moving_averages52, FacebookDailyDates)

        # ALGORITHM FINDINGS
        def clicked():
            messagebox.showinfo('Algorithm Findings',
                                'Crossing Average Intersections: ' + str(len(intersections)) + '\n'
                                    + "Intersection Dates: " + '\n' + str( intersections))

        button2 = ttk.Button(self, text="Algorithm Findings", command=clicked)
        button2.pack()










class StockIndicators(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Stock Indicators", font=FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame(InitialPage))
        button1.pack()



        #APPLE

        apple = ttk.Label(self, text="Apple", font=FONT, foreground = 'red')
        apple.pack(pady=17)

        applelabel1 = ttk.Label(self, text="1 Year Estimate Stock Price: " + apple_nextyearest , font=font)
        applelabel1.pack(pady=8, padx=10)

        applelabel2 = ttk.Label(self, text="Return on Assets: " + apple_returnassets, font=font)
        applelabel2.pack(pady=8, padx=10)

        applelabel3 = ttk.Label(self, text="Volume: " + apple_volume, font=font)
        applelabel3.pack(pady=8, padx=10)


        #AMAZON

        amazon = ttk.Label(self, text="Amazon", font=FONT, foreground='red')
        amazon.pack(pady=17)

        amazonlabel1 = ttk.Label(self, text="1 Year Estimate Stock Price: " + amazon_nextyearest, font=font)
        amazonlabel1.pack(pady=8, padx=10)

        amazonlabel2 = ttk.Label(self, text="Return on Assets: " + amazon_returnassets, font=font)
        amazonlabel2.pack(pady=8, padx=10)

        amazonlabel3 = ttk.Label(self, text="Volume: " + amazon_volume, font=font)
        amazonlabel3.pack(pady=8, padx=10)


        #FACEBOOK

        facebook = ttk.Label(self, text="Facebook", font=FONT, foreground='red')
        facebook.pack(pady=17)

        facebooklabel1 = ttk.Label(self, text="1 Year Estimate Stock Price: " + facebook_nextyearest, font=font)
        facebooklabel1.pack(pady=8, padx=10)

        facebooklabel2 = ttk.Label(self, text="Return on Assets: " + facebook_returnassets, font=font)
        facebooklabel2.pack(pady=8, padx=10)

        facebooklabel3 = ttk.Label(self, text="Volume: " + facebook_volume, font=font)
        facebooklabel3.pack(pady=8, padx=10)

        #TESLA

        tesla = ttk.Label(self, text="Tesla", font=FONT, foreground='red')
        tesla.pack(pady=17)

        teslalabel1 = ttk.Label(self, text="1 Year Estimate Stock Price: " + tesla_nextyearest, font=font)
        teslalabel1.pack(pady=8, padx=10)

        teslalabel2 = ttk.Label(self, text="Return on Assets: " + tesla_returnassets, font=font)
        teslalabel2.pack(pady=8, padx=10)

        teslalabel3 = ttk.Label(self, text="Volume: " + tesla_volume, font=font)
        teslalabel3.pack(pady=8, padx=10)




        #PICTURES

        load = Image.open('pictures/stockind.png')
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=950, y=300)

        load1 = Image.open('pictures/globe.png')
        render1 = ImageTk.PhotoImage(load1)

        img1 = Label(self, image=render1)
        img1.image = render1
        img1.place(x=50, y=275)








app = StockAnalysis()
app.mainloop()