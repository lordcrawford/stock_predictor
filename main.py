import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style

import tkinter as tk
from tkinter import ttk

from AppleStock import AppleDates,ApplePrices, AppleCurrentPrice, \
    AppleDailyPrices, AppleDailyDates, apple_moving_averages13, apple_moving_averages52
from AmazonStock import AmazonDates, AmazonPrices, AmazonDailyDates,\
    AmazonDailyPrices, AmazonCurrentPrice, amazon_moving_averages13, amazon_moving_averages52
from TeslaStock import TeslaDates, TeslaPrices, TeslaDailyDates,\
    TeslaDailyPrices, TeslaCurrentPrice, tesla_moving_averages13, tesla_moving_averages52


LARGE_FONT = ("Verdana", 12)
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

        for F in (InitialPage, AmazonStock, TeslaStock, AppleStock):

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
        label = ttk.Label(self, text = "Initial Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Apple Stock", command=lambda: controller.show_frame(AppleStock))
        button1.pack()

        button2 = ttk.Button(self, text = "Amazon Stock", command=lambda: controller.show_frame(AmazonStock))
        button2.pack()

        button3 = ttk.Button(self, text="Tesla Stock", command=lambda: controller.show_frame(TeslaStock))
        button3.pack()










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




app = StockAnalysis()
app.mainloop()