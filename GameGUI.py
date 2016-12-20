from tkinter import *
from tkinter import ttk
from array import array

class Game:
    
    def __init__(self,master):

#main frame
        master.minsize(width=800,height=600)
        master.resizable(0, 0)
        master.title("Game")
        master.configure(bg='#000')

#buttons
        self.enter=ttk.Button(master,text="enter",width=10,command=self.enter)
        self.enter.pack()
        self.enter.place(x=150, y=500,anchor=CENTER)
        
        self.shuffle=ttk.Button(master,text="shuffle",width=10, command=self.shuffle)
        self.shuffle.pack()
        self.shuffle.place(x=350,y=500,anchor=CENTER)
        
        self.getnew=ttk.Button(master,text="New",width=10,command=self.generate)
        self.getnew.pack()
        self.getnew.place(x=550,y=500,anchor=CENTER)

        self.labels(6,6,master)


#labels
  

    def labels(s, number, self,master):
        labels=[]
         
        for i in range (0,number):
            labels.append(ttk.Label(master))
            labels[i].pack()
            
        for i in range (0,number):
            labels[i].place(x=i*100+150,y=400,anchor=CENTER)
            labels[i].configure(height=20,width=25)
            
            
    
    def enter(self):
        print("enter")


    def shuffle(self):
        print("shuffle")


    def generate(self):
        print("generate")


def main():
    root=Tk()
    mygame=Game(root)
    root.mainloop()
if __name__ == "__main__": main()
        
        
