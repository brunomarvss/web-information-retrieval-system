#!/usr/bin/env python2.7
from Tkinter import *
import tkMessageBox
from search import Search
from htmlparser import htmlParser
from nltk.tokenize import sent_tokenize
from ScrolledText import ScrolledText
import webbrowser
from word_graph import Graph
class gui:

    def __init__(self):
        self.master = Tk()
        self.master.geometry("800x600+100+10")
        self.master.title("WIReS - Web Information Retrieval System")
        self.master.configure(background='white')
        self.master.resizable(width=FALSE, height=FALSE)

    ########################################################################################################
    def guimain(self):

        global query
        query = StringVar(None)
        self.label1 = Label(self.master, text="WIReS", font=('Impact',70),bg='white')
        self.label2 = Label(self.master, text="   SEARCH ENGINE", bg ='#008080', fg='white', font=('arial',7))
        self.lineLabel = Label(self.master,text="____________________________",fg='red',bg='red', font =('arial',7))
        self.helpLabel = Label(self.master, text="HELP", font=('Courier',10))
        self.privLabel = Label(self.master, text="PRIVACY|", font=('Courier',10))
        self.devsLabel = Label(self.master, text="DEVS|", font=('Courier',10))
        self.searchEntry = Entry(self.master, width='50', relief='groove', borderwidth='5', font=('Calibri',15), textvariable=query)
        self.searchButton = Button(self.master, text="SEARCH!", width='30')
        self.clearButton = Button(self.master, text="CLEAR FIELD")
        #locs
        self.label1.place(x=300,y=150)
        self.label2.place(x=455,y=250)
        self.lineLabel.place(x=310,y=250)
        self.searchEntry.place(x=180,y=320)
        self.searchButton.place(x=400,y=400)
        self.clearButton.place(x=250, y=400)
        self.devsLabel.place(x=690,y=570)
        self.helpLabel.place(x=733,y=570)
        self.privLabel.place(x=625, y=570)

        self.searchEntry.focus_set()

        def clearBtn(event):
            self.searchEntry.delete(0,END)
            self.searchEntry.focus_set()
            return

        #events
        self.clearButton.bind("<Button-1>",clearBtn)
        self.searchButton.bind("<Button-1>",self.searchBtn)

    def searchBtn(self, event):
        try:
            global query
            query = StringVar(None)
            search_ = Search()
            query = self.searchEntry.get()
            query = ' '.join(query.split())
            if query not in (None, '', ' '):    ##### condition; butas pag madaming whitespace
                global title_url
                title_url = [None]
                raw = search_.fetch_url(query)
                title_url = search_.process_url(raw)
                self.master.withdraw()
                self.guiresults()
            else:
                tkMessageBox.showinfo('Info', 'You must put a keyword')
        except Exception as e:
                tkMessageBox.showinfo('Info', 'No Internet Connection Try Again Later')

####################

    def guiresults(self):
        
        global q_String
        q_String = StringVar()
        
        self.masters = Tk()
        self.masters.geometry("1100x700+100+10")
        self.masters.title("WIReS - Web Information Retrieval System")
        self.masters.configure(background='white')
        self.masters.resizable(width=FALSE, height=FALSE)

        self.searchEntry1 = Entry(self.masters, width='50', relief='groove', borderwidth='5', font=('Calibri',15))
        self.searchButton = Button(self.masters, text="SEARCH!", width='30')
        self.clearButton1 = Button(self.masters, text="CLEAR FIELD", width='20')
        self.labelss = Label(self.masters, text="SEARCH RESULTS:", bg ='#008080', fg='white', font=('arial',10))
        self.resultframe = LabelFrame(self.masters,text="PAGE RESULT",height=540, width=990,relief = "groove", bg ="white")
        self.result_label = ScrolledText(self.resultframe,width = 120, height = 32,bg = 'white', undo = True)
        self.graphButton = Button(self.masters, text="Graphs", width='8')
        
        #URL
        self.labelres1 = Label(self.masters, text = title_url[0][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres1= Label(self.masters, text = title_url[0][1], fg="blue", cursor="hand2", bg="white")
        self.labelres2 = Label(self.masters, text = title_url[1][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres2 = Label(self.masters, text = title_url[1][1], fg="blue", cursor="hand2", bg="white")
        self.labelres3 = Label(self.masters, text = title_url[2][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres3 = Label(self.masters, text = title_url[2][1], fg="blue", cursor="hand2", bg="white")
        self.labelres4 = Label(self.masters, text = title_url[3][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres4 = Label(self.masters, text = title_url[3][1], fg="blue", cursor="hand2", bg="white")
        self.labelres5 = Label(self.masters, text = title_url[4][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres5 = Label(self.masters, text = title_url[4][1], fg="blue", cursor="hand2", bg="white")
        self.labelres6 = Label(self.masters, text = title_url[5][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres6 = Label(self.masters, text = title_url[5][1], fg="blue", cursor="hand2", bg="white")
        self.labelres7 = Label(self.masters, text = title_url[6][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres7 = Label(self.masters, text = title_url[6][1], fg="blue", cursor="hand2", bg="white")
        self.labelres8 = Label(self.masters, text = title_url[7][0], font=('arial 13 bold'), bg="white", cursor="hand2")
        self.linkres8 = Label(self.masters, text = title_url[7][1], fg="blue", cursor="hand2", bg="white")

        #gui2 loc
        self.searchEntry1.place(x=15,y=15)
        self.searchButton.place(x=550,y=18)
        self.labelss.place(x=15,y=60)
        self.labelres1.place(x=15,y=110)
        self.linkres1.place(x=15,y=140)
        self.labelres2.place(x=15,y=170)
        self.linkres2.place(x=15,y=200)
        self.labelres3.place(x=15,y=230)
        self.linkres3.place(x=15,y=260)
        self.labelres4.place(x=15,y=290)
        self.linkres4.place(x=15,y=320)
        self.labelres5.place(x=15,y=350)
        self.linkres5.place(x=15,y=380)
        self.labelres6.place(x=15,y=410)
        self.linkres6.place(x=15,y=440)
        self.labelres7.place(x=15,y=470)
        self.linkres7.place(x=15,y=500)
        self.labelres8.place(x=15,y=530)
        self.linkres8.place(x=15,y=560)
        self.clearButton1.place(x=800,y=18)
        


        self.searchEntry1.insert(END,query)

        def showGraph(event):
            graph = Graph()
            raws = StringVar()
            raws = self.result_label.get(1.0, END)
            
            graph.plot_word(raws)

            
        def clearBtn1(event):
            self.searchEntry1.delete(0,END)
            self.searchEntry1.focus_set()
            return

        #destroy func
        def destroyresult(self):
            self.labelss.destroy(),self.linkres1.destroy(),self.labelres1.destroy(),self.linkres2.destroy()
            self.labelres2.destroy(),self.linkres2.destroy(),self.labelres2.destroy(),self.linkres3.destroy()
            self.labelres3.destroy(),self.linkres4.destroy(),self.labelres4.destroy(),self.linkres5.destroy()
            self.labelres5.destroy(),self.linkres6.destroy(),self.labelres6.destroy(),self.linkres7.destroy()
            self.labelres7.destroy(),self.linkres8.destroy(),self.labelres8.destroy()

        #eventfunc
        def callback1(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[0][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')

            self.graphButton.place(x = 980, y=18)
      
        def callback2(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[1][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')

            self.graphButton.place(x = 980, y=18)
           


        def callback3(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[2][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
   

        def callback4(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[3][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')

            self.graphButton.place(x = 980, y=18)

        def callback5(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[4][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)

            self.result_label.place(x = 1, y = 1)

            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')

            self.graphButton.place(x = 980, y=18)

        def callback6(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[5][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')


            self.graphButton.place(x = 980, y=18)

        def callback7(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[6][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.graphButton.place(x = 980, y=18)

        def callback8(event):
            html_parse = htmlParser()
            raw = html_parse.clean_html(html_parse.url_opener(title_url[7][1]))
            destroyresult(self)
            self.resultframe.place(x=15,y=80)
            self.result_label.place(x = 1, y = 1)
            self.result_label.insert(END,raw)
            self.result_label.configure(state = 'disabled')
            self.graphButton.place(x = 980, y=18)

        def searchAction(event):
            try:
                global query
                query = StringVar(None)
                search_ = Search()
                query = self.searchEntry1.get()
                query = ' '.join(query.split())

                if query is not(None, '', ' '):
                    global title_url
                    title_url = [None]
                    raw = search_.fetch_url(query)
                    title_url = search_.process_url(raw)
                    self.masters.withdraw()
                    self.guiresults()


                else:
                    tkMessageBox.showinfo('Info', 'You must put a keyword')
            except Exception as e:
                    tkMessageBox.showinfo('Info', 'No Internet Connection Try Again Later')





        #eventlink
        self.graphButton.bind("<Button-1>", showGraph)
        self.searchButton.bind("<Button-1>",searchAction)
        self.linkres1.bind("<Button-1>", callback1)
        self.linkres2.bind("<Button-1>", callback2)
        self.linkres3.bind("<Button-1>", callback3)
        self.linkres4.bind("<Button-1>", callback4)
        self.linkres5.bind("<Button-1>", callback5)
        self.linkres6.bind("<Button-1>", callback6)
        self.linkres7.bind("<Button-1>", callback7)
        self.linkres8.bind("<Button-1>", callback8)
        self.labelres1.bind("<Button-1>", callback1)
        self.labelres2.bind("<Button-1>", callback2)
        self.labelres3.bind("<Button-1>", callback3)
        self.labelres4.bind("<Button-1>", callback4)
        self.labelres5.bind("<Button-1>", callback5)
        self.labelres6.bind("<Button-1>", callback6)
        self.labelres7.bind("<Button-1>", callback7)
        self.labelres8.bind("<Button-1>", callback8)
        self.clearButton1.bind("<Button-1>", clearBtn1)

        self.searchEntry1.insert(END,'')


def main():
    master1 = gui()
    master1.guimain()
    master1.master.mainloop()

if __name__=='__main__':
    main()
