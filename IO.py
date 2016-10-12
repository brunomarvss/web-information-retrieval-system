from Tkinter import *



class gui:

    def __init__(self):
        self.master = Tk()
        self.master.geometry("800x600+100+10")
        self.master.title("WIReS - Web Information Retrieval System")
        self.master.configure(background='white')
        self.master.resizable(width=FALSE, height=FALSE)


    def guimain(self):
        v1 = StringVar()
        def get_data(event):
            print 'haha'
        searchEntry = Entry(self.master, width='50', relief='groove', textvariable=v1,borderwidth='5', font=('Calibri',15))
        searchButton = Button(self.master, text="SEARCH!", width='30')
        searchButton.bind("<Button-1>",get_data)
        
        #locs

        
        searchEntry.place(x=180,y=320)
        searchButton.place(x=400,y=400)
        


        searchEntry.focus_set()




master1 = gui()
master1.guimain()

master1.master.mainloop()
