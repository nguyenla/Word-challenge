from tkinter import *
from tkinter.ttk import *
from GameModel import *
from PIL import Image, ImageTk
from PIL import *

class GameEndView(Frame):

    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        
    #main frame
        s = Style()
        s.theme_use('alt')
        self.master.minsize(width = 700, height = 600)
        self.master.title("Game")
        self.master.configure(background='#23B6C0')
        
        
        self.image = Image.open('snowflakes.jpg')
        self.image_copy = self.image.copy()
        
        self.resized = self.image.resize((800,700)) # resized image-gets the size of the whole frame
        self.resized2 = ImageTk.PhotoImage(self.resized) # creates the photo image from the file
        self.back = Label(self.master, image = self.resized2, anchor = CENTER) # sets the image
        self.back.pack(fil = BOTH, expand = YES)
    

        label = Label(self.master, text = "Game Over")
        label.pack()
        # BUTTONS ON VIEW
        
        bstyle=Style()
        bstyle.configure('B.TButton',background='red')
        
        # Enter button
        self.enter=Button(self.master,text="enter",width=6)
        self.enter.pack()
        self.enter.place(x=400, y=600,anchor=CENTER)
        self.enter.configure(style='B.TButton')

        # Shuffle button
        self.shuffle=Button(self.master,text="shuffle",width=6)
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=500,y=600,anchor=CENTER)

        # New button
        self.getnew=Button(self.master,text="New",width=6)
        self.getnew.pack()
        self.getnew.place(x=600,y=600,anchor=CENTER)


    
def main():
    master = Tk()
#     controller = GameController()
#     mygame=GameEndView(master, controller)
#     mygame.master.mainloop()
if __name__ == "__main__": main()