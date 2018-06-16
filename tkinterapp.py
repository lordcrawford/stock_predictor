from tkinter import *
import webbrowser


#root = Tk()

#theLabel = Label(root, text = "Stock Analysis" )
#theLabel.pack()

#root.mainloop()

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self,master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("GUI")

        self.pack(fill=BOTH, expand=1)

        #quitButton = Button(self, text="Quit", command = self.client_exit)
        #quitButton.place(x=0, y=0)

        #MENU

        menu = Menu(self.master)
        self.master.config(menu=menu)


        #FILE TAB ON MENU
        file = Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)




        #EDIT TAB ON MENU
        edit = Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)



        #HELP TAB ON MENU
        help = Menu(menu)

        new = 1
        url = "https://finance.yahoo.com/"

        def openweb():
            webbrowser.open(url, new=new)


        help.add_command(label="Yahoo Finance Website", command = openweb)
        menu.add_cascade(label="Help", menu=help)



    def client_exit(self):
        exit()



root = Tk()

root.geometry("400x300")

app = Window(root)

root.mainloop()
