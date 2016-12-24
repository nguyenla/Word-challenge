from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from GameModel import *
import sys
class Game():

    def __init__(self):
        self.model=GameModel()
        self.master = Tk()
        self.controller = None
        
         # labels for letter
        self.randomlet=[]
        self.randomlet=self.labels(self.master,20,6,400,60,60,65,'#008B8B')

        self.enteredlet=[]
        self.enteredlet=self.labels(self.master,20,6,300,60,60,65,'#FFEBCD')
        
    #main frame
        s=Style()
        s.theme_use('alt')
        self.master.minsize(width=800,height=600)
        self.master.resizable(0, 0)
        self.master.title("Game")
        self.master.configure(background='#23B6C0')

    #score
        self.score=Label(self.master, text='Score: 0',foreground='black',background='red')
        self.score.pack()
        self.score.place(x=50,y=50)

        #timer
        self.timer=Label(self.master,text="2:00",background='blue')
        self.timer.pack()
        self.timer.place(x=650,y=50)
        self.timer.configure(foreground='yellow')




#buttons

        # To-do: Review
        self.time_remaining = 120


        #buttons
        bstyle=Style()
        bstyle.configure('B.TButton',background='red')

        self.enter=Button(self.master,text="enter",width=5,command=self.enter_function)
        self.enter.pack()
        self.enter.place(x=250, y=550,anchor=CENTER)
        self.enter.configure(style='B.TButton')

        self.shuffle=Button(self.master,text="shuffle",width=5,command=self.display_curKey(self.model.curKey))
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=350,y=550,anchor=CENTER)

        self.getnew=Button(self.master,text="New",width=5)
        self.getnew.pack()
        self.getnew.place(x=450,y=550,anchor=CENTER)

        self.start=Button(self.master,text="Start",width=5)
        self.start.pack()
        self.start.place(x=150,y=550,anchor=CENTER)

       
      
        

        # labels for words
        self.words3=[]
        for i in range (0, 10):
            self.words3.append(self.labels(self.master,1,3,i*25+30,15,120,65,'#CCFFFF'))
        self.words4=[]
        for i in range (0, 10):
            self.words4.append(self.labels(self.master,1,4,i*25+30,15,240,65,'#CCFFFF'))

        self.words5=[]
        for i in range (0, 10):
            self.words5.append(self.labels(self.master,1,5,i*25+30,15,360,65,'#CCFFFF'))

        self.words6=[]
        for i in range (0, 10):
            self.words6.append(self.labels(self.master,1,6,i*25+30,15,480,65,'#CCFFFF'))
    
        # binding keys to buttons
        self.master.bind("<Return>", self.enter_function)
        self.master.bind("<space>", self.shuffle_function)
        self.master.bind("<Key>", self.key)
    
    
    
    
    def register_controller(self, controller):
        self.controller = controller



    # To-do: CATA please help me implement
    # key: 6-character key to be displayed on the lower level
    def display_curKey(self,key):  
        letters=list(key)
        for i in range (0,6): 
           self.randomlet[i].configure(text=letters[i])
           
    
         
    # To-do: CATA please help me implement
    # This function displays a character on the upper level 
    def type_character(self, word):
        if(len(word)==3):
            for rows in self.words3:
                if(rows[0]['text']=='_'):
                    for i in range (0,3):
                        key=word[i]
                        rows[i].configure(text=key, background='#191970',foreground='white')
                    break
        if(len(word)==4):
            for rows in self.words4:
                if(rows[0]['text']=='_'):
                    for i in range (0,4):
                        key=word[i]
                        rows[i].configure(text=key, background='#191970',foreground='white')
                    break
        if(len(word)==5):
            for rows in self.words5:
                if(rows[0]['text']=='_'):
                    for i in range (0,5):
                        key=word[i]
                        rows[i].configure(text=key, background='#191970',foreground='white')
                    break 
        if(len(word)==6):
            for rows in self.words6:
                if(rows[0]['text']=='_'):
                    for i in range (0,6):
                        key=word[i]
                        rows[i].configure(text=key, background='#191970',foreground='white')
                    break               


    # s: size of the label
    # number: how many letters
    # pos: vertical position of the label
    # dist: distance between two adjacent columns
    # start: horizontal position of the first column
    # word: character to be displayed on the label
    def labels(self, master, s, number, pos, dist, start, word, color):
        labels=[]
        for i in range (0,number):
            labels.append(Label(master,text='_',padding=s))
            labels[i].pack()
            prev=start
            labels[0].place(x=prev, y= int(pos))
        for i in range (0,number):
            prev=prev+s+dist
            labels[i].place(x=prev,y=int(pos))
            labels[i].configure(padding=s, background=color)
        return labels

    # To-do: CATA please help me implement
    # This function takes the word from the upper level and send to the controller
    def enter_function(self, event = None):        
        # Get the word input by the player 
        word=[]
        for let in self.enteredlet:
            key=let['text']
            if(key!='_'):
                word.append(key)
        playword=''
        for i in range (0,len(word)):
            playword=playword+word[i]
        val=self.controller.play_word(playword)
        print(val)
        if (val>=0): 
            self.type_character(playword)
            self.update_score
        self.reset_input
        print("Send a word to the controller")
        
        
    def shuffle_function(self, event = None):
        print("shuffle")

    def generate(self):
        self.controller.increase_time(3)
        print("generate")

    def update_score(self):
        new_score = self.controller.score
        self.score.configure(text='Score: '+str(new_score))


    def update_clock(self, count):      
        self.timer['text'] = count
        if count > 0:
            print(count)
            self.master.after(1000, self.update_clock(count-1))


    # To-do: Implement this method
    # Resetting the input area
    def reset_input(self):
        for let  in self.enteredlet:
            key=let['text']
            for word in self.randomlet:
                if(word['text']=='_'):
                    word.configure(text=key,background='#008B8B',foreground='white')
                    let.configure(text='_',background= '#FFEBCD')
                    break
        
        

    def start_timer(self):
        self.controller.start_timer()
    
    def display_time(self, time):
        if time < 0:
            self.timer.configure(text = "Time's Up!")
        else:
            mins = time // 60
            secs = time % 60
            secstr = ""
            if secs < 10:
                secstr = '0' + str(secs)
            else:
                secstr = str(secs)
            self.timer.configure(text = str(mins) + ":" + secstr)



    def key(self, event):
        # Make sure the frame is receiving input!
        #self.master.focus_force()
        key=event.keysym
        check=False
        for ran in self.randomlet:
            if (ran['text']==key):
                check=True
                ran.configure(text="_",background='#F8F8FF')
                for let in self.enteredlet:
                    if (let['text']=="_"):
                        let.configure(text=key,background='pink',foreground='black')
                        
                        break
                break
        if (check==False):
            messagebox.showerror("Error","This letter is not available.\nTry again")
        
    
def main():
    mygame=Game()
    mygame.master.mainloop()
    
if __name__ == "__main__": main()