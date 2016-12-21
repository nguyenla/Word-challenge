from tkinter import *
from tkinter.ttk import *

class Game():

    def __init__(self):
        self.master = Tk()
        self.controller = None

    #main frame
        s=Style()
        s.theme_use('alt')
        self.master.minsize(width=800,height=600)
        self.master.resizable(0, 0)
        self.master.title("Game")
        self.master.configure(background='#23B6C0')


#score

        self.score=Label(self.master, text='',foreground='blue',background='red')
        self.score.pack()
        self.score.place(x=50,y=50)



#timer
        self.timer=Label(self.master,text="10",background='blue')
        self.timer.pack()
        self.timer.place(x=650,y=50)
        self.timer.configure(foreground='yellow')

# To-do: Review
        self.time_remaining = 0

#buttons

        bstyle=Style()
        bstyle.configure('B.TButton',background='red')

        self.enter=Button(self.master,text="enter",width=5,command=self.enter)
        self.enter.pack()
        self.enter.place(x=250, y=550,anchor=CENTER)
        self.enter.configure(style='B.TButton')

        self.shuffle=Button(self.master,text="shuffle",width=5, command=self.shuffle)
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=350,y=550,anchor=CENTER)

        self.getnew=Button(self.master,text="New",width=5,command=self.generate)
        self.getnew.pack()
        self.getnew.place(x=450,y=550,anchor=CENTER)

        self.start=Button(self.master,text="Start",width=5,command=self.start_timer)
        self.start.pack()
        self.start.place(x=150,y=550,anchor=CENTER)

        #labels for letter

        self.labels(self.master,20,6,400,60,60,65)
        self.labels(self.master,20,6,300,60,60,65)

        #labels for words
        self.words3=[]
        for i in range (0, 10):
                self.words3.append(self.labels(self.master,1,3,i*25+30,15,120,65))
        words4=[]
        for i in range (0, 10):
                words4.append(self.labels(self.master,1,4,i*25+30,15,240,65))

        words5=[]
        for i in range (0, 10):
                words5.append(self.labels(self.master,1,5,i*25+30,15,360,65))

        words6=[]
        for i in range (0, 10):
            words6.append(self.labels(self.master,1,6,i*25+30,15,480,65))

    def register_controller(self, controller):
        self.controller = controller

    # To-do: CATA please help me implement
    # key: 6-character key to be displayed on the lower level
    def display_curKey(self, key):
        print(key)
   
    # To-do: CATA please help me implement
    # This function displays a character on the upper level 
    def type_character(self):
        print("Typing")


    # s: size of the label
    # number: how many letters
    # pos: vertical position of the label
    # dist: distance between two adjacent columns
    # start: horizontal position of the first column
    # word: character to be displayed on the label
    def labels(self,master,s, number,pos,dist,start,word):
        labels=[]
        for i in range (0,number):
            labels.append(Label(master,text='_',padding=s))
            labels[i].pack()
            prev=start
            labels[0].place(x=prev, y= int(pos))
        for i in range (0,number):
            prev=prev+s+dist
            labels[i].place(x=prev,y=int(pos))
            labels[i].configure(padding=s)
        return labels

    # To-do: CATA please help me implement
    # This function takes the word from the upper level and send to the controller
    def enter(self):
        print("Send a word to the controller")

    def shuffle(self):
        print("shuffle")


    def generate(self):
        print("generate")

    def update_score(self):
        new_score = self.controller.score
        self.score.configure(text='Score: '+str(new_score))

    def start_timer(self):
        self.update_clock(120)

    def update_clock(self, remaining = None):
        if remaining is not None:
            self.time_remaining = remaining

        if self.time_remaining <= 0:
            self.timer.configure(text = "Time's Up")
        else:
            self.timer.configure(text = "%d" % self.time_remaining)
            self.time_remaining -= 1
            self.master.after(1000, self.update_clock)

def main():
    mygame=Game()
    mygame.master.mainloop()

if __name__ == "__main__": main()
