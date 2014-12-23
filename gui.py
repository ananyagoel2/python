import Tkinter

from final import *

class myapp(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):

        top1=Tkinter.Label(self,text="CHATTERBOT",fg="red",font=("Times New Roman",12))
        top1.grid(row=0,column=0)
        top2=Tkinter.Label(self,text="By Group 1",fg="black",font=("Times New Roman",8))
        top2.grid(row=1,column=0)
        top3=Tkinter.Label(self)
        top3.grid(row=2,pady=8)

        
        self.entryvar1=Tkinter.StringVar()
        entry1=Tkinter.Entry(self,textvariable=self.entryvar1)
        entry1.grid(row=3,columnspan=2)

        self.entryvar2=Tkinter.StringVar()
        self.output=Tkinter.Text(self)
        self.output.grid(row=12)

        self.output.insert(Tkinter.INSERT, "Hello! I am the CIC chatbot!")
        self.output.insert(Tkinter.INSERT, "\nIt's nice to see you here!")
        self.output.insert(Tkinter.INSERT, "\nHow may i help you?")

        btn1=Tkinter.Button(self,text="Get Answer!",command=self.working)
        btn1.grid(row=3,column=1)
        
        self.geometry('800x600')


    def working(self):
        inp=self.entryvar1.get()
        self.output.insert(Tkinter.END, "\n"+chatbot(inp))


        







if __name__ =="__main__":
    app=myapp(None)
    app.title('Chatterbot')
    app.mainloop()
