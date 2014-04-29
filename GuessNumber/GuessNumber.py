#Guessing Game in Python
#Marvin Trilles

from tkinter import *
from tkinter.ttk import *

import random

class GuessingGame(Frame):

    guessNumber = 0
    remainingTry = 0
    maxNumber = 0
    
    def __init__(self,master=None):

        Frame.__init__(self,master)
        
        self.master.title("Guess The Number")
        
        """Display the main window"
        with a little bit of padding"""
        self.grid(padx=10,pady=10)
        self.CreateWidgets()
        self.Range100(None)
       
    def CreateWidgets(self):
        
        self.result=StringVar()
        self.rangeVal=StringVar()
        self.remainingTryDisplay =StringVar()
        self.lastGuessesValue=StringVar()
       
        
        self.buttonRange100 = Button(self,text="Range 1-100",width=50)
        self.buttonRange100.grid(row=0, column=0)

        self.buttonRange1000 = Button(self,text="Range 1-1000", width=50)
        self.buttonRange1000.grid(row=1, column=0)

        self.labelInstruction = Label(self, text ="Enter your guess :")
        self.labelInstruction.grid(row=2,column=0, sticky=NW)

        self.textGuess = Entry(self,takefocus=TRUE)
        self.textGuess.grid(row=3,column=0, sticky=NW)

        self.labelResult = Label(self, text ="-------", textvariable=self.result)
        self.labelResult.grid(row=3,column=0, sticky=NE)

        self.labelRange = Label(self,text="Range :")
        self.labelRange.grid(row=4,column=0,sticky=NW)

        self.labelRangeValue = Label(self,textvariable=self.rangeVal)
        self.labelRangeValue.grid(row=4,column=0,sticky=NE)

        self.labelRemaining = Label(self,text="Remaining Try :")
        self.labelRemaining.grid(row=5,column=0,sticky=NW)

        self.labelRemainingValue = Label(self,textvariable=self.remainingTryDisplay)
        self.labelRemainingValue.grid(row=5,column=0,sticky=NE)

        self.lastGuesses = Label(self,textvariable =self.lastGuessesValue)
        self.lastGuesses.grid(row=6,column=0,sticky=NW)

        self.buttonRange100.bind("<Button-1>",self.Range100)
        self.buttonRange1000.bind("<Button-1>",self.Range1000)
        self.textGuess.bind("<Return>",self.GetResult)
        self.textGuess.focus()

    def new_game(self):
        self.rangeVal.set("1 to " + str(self.maxNumber))
        self.remainingTryDisplay.set(str(self.remainingTry))
        self.lastGuessesValue.set("")
        self.textGuess.focus()

    def restart_game(self):
        self.result.set("")
        self.textGuess.focus()
        if self.maxNumber == 100:
            self.Range100(self)
        else:
            self.Range1000(self)
        

    def Range100(self,event):
        self.maxNumber = 100
        self.guessNumber = random.randint(0,100)
        self.remainingTry = 7
        self.new_game()
        self.textGuess.focus()

    def Range1000(self,event):
        self.maxNumber = 1000
        self.guessNumber = random.randint(0,1000)
        self.remainingTry = 10
        self.new_game()
        self.textGuess.focus()

    def GetResult(self,event):
        inputValue =int(self.textGuess.get())
       
        self.textGuess.delete(0,len(self.textGuess.get()))
        self.textGuess.focus()

        if inputValue> self.guessNumber:
            self.result.set("Lower!!")
            self.lastGuessesValue.set( self.lastGuessesValue.get() + " " +str(inputValue))
        elif inputValue< self.guessNumber:
            self.result.set("Higher!!")
            self.lastGuessesValue.set( self.lastGuessesValue.get() + " " +str(inputValue))
        else:
            messagebox.showinfo("Congratulations","You guessed " + str(self.guessNumber)+ " correctly.")
            self.restart_game()
            return
        
        self.remainingTry = self.remainingTry - 1
        
        if self.remainingTry == 0:
            messagebox.showerror("Sorry","You ran out of tries. The number is "+ str(self.guessNumber)+".")
            self.restart_game()

        else:
            self.remainingTryDisplay.set(str(self.remainingTry))
        
      
                
if __name__ == "__main__":
    game = GuessingGame()
    game.mainloop()
