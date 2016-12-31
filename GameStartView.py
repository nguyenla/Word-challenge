
from tkinter.ttk import *
from tkinter import *
from PIL import Image, ImageTk
from PIL import *
from GameController import GameController
class GameStartView(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.imgfileinit=Image.open('start.png')
        self.imgfile=self.imgfileinit.resize((80,80),Image.ANTIALIAS)
        self.photo=ImageTk.PhotoImage(self.imgfile)
        
        s = Style()
        s.theme_use('alt')
    
        
        self.startButton = Button(self.master, text = 'Start', command = self.start_game, image=self.photo)
        self.startButton.pack()
        self.startButton.place(x=360,y=230)
     #   self.pack()
        
        self.name=Label(text='Word Challenge',background='#23B6C0',anchor='w')
        self.name.configure(font=('Helvetica',65),foreground='yellow')
        self.name.pack()
        self.name.place(x=200, y=80)
        
        self.instr=Label(text='Instructions: \n\n\nPress TAB to get a new letter combination \n\nPress SPACEBAR to Shuffle the letters \n\nPress ENTER to enter the word \n\nPress BACKSPACE to delete letters',background='#23B6C0',anchor='w')
        self.instr.configure(font=('Helvetica',20),foreground='white')
        self.instr.pack()
        self.instr.place(x=220, y=350)
        
    def start_game(self):
        self.controller.create_game()
     
    # This function binds a controller to this view
    def register_controller(self, controller):
        self.controller = controller
        
def main():
    root = Tk()
    mygame = GameStartView(root)
    root.mainloop()

if __name__ == "__main__": main()