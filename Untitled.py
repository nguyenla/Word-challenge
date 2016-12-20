from tkinter import *
from tkinter import ttk

class LamApp:
    def __init__(self,master):
        self.label = Label(master, text = "I want to play sport!")
        self.label.grid(row = 0, column = 0, columnspan = 2)
        self.sport1 = Button(master, text = "Soccer", command = self.playSoccer)
        self.sport1.grid(row = 1, column = 0)
        self.sport2 = Button(master, text = "Basketball", command = self.playBasketball)
        self.sport2.grid(row = 1, column = 1)
        
    def playSoccer(self):
        self.label["text"] = "I want to play soccer"

    def playBasketball(self):
        self.label["text"] = "I want to play basketball"
        
def main():
    root = Tk()
    app = LamApp(root)
    root.mainloop()

if __name__ == "__main__": main()
