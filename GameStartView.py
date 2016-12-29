from GameController import GameController
from tkinter import *

class GameStartView(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.master = master
        self.startButton=Button(self, text='Start', command=self.start_game)
        self.startButton.pack()
        self.pack()
        self.controller = None
    
    def start_game(self):
        self.controller.create_game()
     
    # This function binds a controller to this view
    def register_controller(self, controller):
        self.controller = controller
        
def main():
    root=Tk()
    mygame=GameStartView(root)
    root.mainloop()

if __name__ == "__main__": main()