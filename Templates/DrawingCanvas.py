#Timer Game in Python
#Marvin Trilles

from tkinter import *
from tkinter.ttk import *
from threading import *

import random

class TimerGame(Frame):

    def __init__(self,master=None):

        Frame.__init__(self,master)
        
        self.master.title("Timer Game")
        
        self.grid(padx=10,pady=10)
        self.CreateWidgets()
       
    def CreateWidgets(self):
        
        #self.buttonRange100 = Button(self,text="Range 1-100",width=50)
        #self.buttonRange100.grid(row=0, column=0)
        #self.buttonRange100.bind("<Button-1>",self.Range100)

        self.frameControls = Frame(self,width=30, height=300)
        self.frameControls.grid(row=0,column=0,sticky="NW")
        
        self.frameCanvas = Frame(self,width=400, height=200)
        self.frameCanvas.grid(row=0,column=1,sticky="NW")

        self.buttonStart = Button(self.frameControls, text="Start",width=30)
        self.buttonStart.pack(side="bottom")

        self.buttonStop = Button(self.frameControls, text="Stop",width=30)
        self.buttonStop.pack(side="bottom")

        self.buttonRestart = Button(self.frameControls, text="Restart",width=30)
        self.buttonRestart.pack(side="bottom")
        
        self.mainCanvas = Canvas(self.frameCanvas,bg="blue")
        self.mainCanvas.pack(fill=X)
        
        
      
                
if __name__ == "__main__":
    game = TimerGame()
    game.mainloop()
