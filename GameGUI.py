from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from GameModel import *
import random

class Game():

    def __init__(self):
        self.model=GameModel()
        self.master = Tk()
        self.controller = None
        
        # labels for letter
        self.randomlet=[]
        self.randomlet=self.labels(self.master,25,6,500,60,150,70,'#008B8B')

        self.enteredlet=[]
        self.enteredlet=self.labels(self.master,25,6,400,60,150,70,'#FFEBCD')
        
    #main frame
        s=Style()
        s.theme_use('alt')
        self.master.minsize(width=1000,height=700)
        self.master.resizable(0, 0)
        self.master.title("Game")
        self.master.configure(background='#23B6C0')

    # LABELS ON VIEW
        #score
        self.score=Label(self.master, text='Score: 0',foreground='black',background='red')
        self.score.pack()
        self.score.place(x=50,y=550)

        #timer
        self.timer=Label(self.master,text="2:00",background='blue')
        self.timer.pack()
        self.timer.place(x=800,y=550)
        self.timer.configure(foreground='yellow')

        # BUTTONS ON VIEW
        
        bstyle=Style()
        bstyle.configure('B.TButton',background='red')
        
        # Enter button
        self.enter=Button(self.master,text="enter",width=6,command=self.enter_function)
        self.enter.pack()
        self.enter.place(x=400, y=600,anchor=CENTER)
        self.enter.configure(style='B.TButton')

        # Shuffle button
        self.shuffle=Button(self.master,text="shuffle",width=6,command=self.display_curKey(self.model.curKey))
        self.shuffle.pack()
        self.shuffle.configure(style='green.TButton')
        self.shuffle.place(x=500,y=600,anchor=CENTER)

        # New button
        self.getnew=Button(self.master,text="New",width=6, command = self.get_new_key)
        self.getnew.pack()
        self.getnew.place(x=600,y=600,anchor=CENTER)

        # Start button
        self.start=Button(self.master,text="Start",width=6, command = self.start_timer)
        self.start.pack()
        self.start.place(x=300,y=600,anchor=CENTER)

        # fields that hold labels for words of each length
        self.words3=[]
        self.words4=[]
        self.words5=[]
        self.words6=[]
    
        # binding keys to buttons
        self.master.bind("<Return>", self.enter_function)
        self.master.bind("<space>", self.shuffle_function)
        self.master.bind("<BackSpace>", self.backspace_function)
        self.master.bind("<Key>", self.key)
    
    # This function binds a controller to this view
    def register_controller(self, controller):
        self.controller = controller
        
    
    # Every time a new key is generated, this function is called to generate new blank labels
    # that hold the place for the words that can be formed from the new key
    def create_labels(self):
        # Destroy all the old labels and reset all the fields
        for label in self.words3:
            for l in label:
                l.destroy()
        
        for label in self.words4:
            for l in label:
                l.destroy()
        
        for label in self.words5:
            for l in label:
                l.destroy()
        
        for label in self.words6:
            for l in label:
                l.destroy()
        
        self.words3 = []
        self.words4 = []
        self.words5 = []
        self.words6 = []
        
        # Create label for 3-letter words
        n3=len(self.controller.model.three)
        if(n3>10):
            for i in range (0, 10):
                self.words3.append(self.labels(self.master,1,3,i*25+30,15,200,65,'#CCFFFF'))
            dif=n3-10
            for i in range (0,dif):
                self.words3.append(self.labels(self.master,1,3,i*25+30,15,280,65,'#CCFFFF'))
        else:
            for i in range (0, n3):
                self.words3.append(self.labels(self.master,1,3,i*25+30,15,200,65,'#CCFFFF'))           
       
        # Create label for 4-letter words
        n4=len(self.controller.model.four)
        if(n4>10):
            for i in range (0, 10):
                self.words4.append(self.labels(self.master,1,4,i*25+30,15,400,65,'#CCFFFF'))
            dif=n4-10
            for i in range (0,dif):
                self.words4.append(self.labels(self.master,1,4,i*25+30,15,500,65,'#CCFFFF'))
        else :
            for i in range (0, n4):
                self.words4.append(self.labels(self.master,1,4,i*25+30,15,400,65,'#CCFFFF'))
      
        # Create label for 5-letter words
        n5=len(self.controller.model.five)
        for i in range (0, n5):
            self.words5.append(self.labels(self.master,1,5,i*25+30,15,600,65,'#CCFFFF'))

        # Create label for 6-letter words
        n6=len(self.controller.model.six)
        for i in range (0, n6):
            self.words6.append(self.labels(self.master,1,6,i*25+30,15,700,65,'#CCFFFF'))


    # This function is called to display a given 6-character key on the lower section
    def display_curKey(self, key):  
        letters=list(key)
        for i in range (0,6): 
            self.randomlet[i].configure(text=letters[i])
    
         
    # TO-DO: Peer-review this function
    # This function displays a character on the upper level 
    def type_character(self, word, position):
        if(len(word)==3):
            rows = self.words3[position]
            for i in range (0,3):
                key=word[i]
                rows[i].configure(text=key, background='#191970',foreground='white')

        if(len(word)==4):
            rows = self.words4[position]
            for i in range (0,4):
                key=word[i]
                rows[i].configure(text=key, background='#191970',foreground='white')

        if(len(word)==5):
            rows = self.words5[position]
            for i in range (0,5):
                key=word[i]
                rows[i].configure(text=key, background='#191970',foreground='white')
        
        if(len(word)==6):
            rows = self.words6[position]
            for i in range (0,6):
                key=word[i]
                rows[i].configure(text=key, background='#191970',foreground='white')



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
            playword = playword+word[i]
        
        val = self.controller.play_word(playword)
        print(val)
      
    
    # TO-DO: implemented the backspace function
    def backspace_function(self, event = None):
        for i in range(0,len(self.enteredlet)):
            
            if(self.enteredlet[i]['text']=="_" ):
                for let in self.randomlet:
                    if (let['text']=='_'):
                        let.configure(text=self.enteredlet[i-1]['text'])
                        break
                self.enteredlet[i-1]['text']='_'
                i-=1
            elif(self.enteredlet[i]['text']!="_" and i==len(self.enteredlet)-1):
                for let in self.randomlet:
                    if (let['text']=='_'):
                        let.configure(text=self.enteredlet[i]['text'])
                        break
                self.enteredlet[i]['text']='_'
                i-=1   
    
    
    
    # This function shuffles the six letters of the key word and displays the shuffled key on the view
    def shuffle_function(self, event = None):
        key = list(self.controller.get_curKey())
        random.shuffle(key)
        shuffled = ''.join(key)
        self.display_curKey(shuffled)



    # This function signals the controller to generate a new key for the game 
    def get_new_key(self):
        self.controller.get_new_key()
        
    
    
    # This function updates the score in the view to the most updated score in the controller
    def update_score(self):
        new_score = self.controller.score
        self.score.configure(text='Score: ' + str(new_score))



    # This function updates the time in the view to the most updated time in the controller
    def update_clock(self, count):
        self.timer['text'] = count
        if count > 0:
            print(count)
            self.master.after(1000, self.update_clock(count-1))



    # Resetting the input area
    def reset_input(self):
        for let  in self.enteredlet:
            key=let['text']
            for word in self.randomlet:
                if(word['text']=='_'):
                    word.configure(text=key,background='#008B8B',foreground='white')
                    let.configure(text='_',background= '#FFEBCD')
                    break
        
        
    # This function listens to the key pressed and handles it accordingly
    def key(self, event):
        key=event.keysym
        check = False
        for ran in self.randomlet:
            if (ran['text']==key):
                check=True
                ran.configure(text="_",background='#F8F8FF')
                for let in self.enteredlet:
                    if (let['text']=="_"):
                        let.configure(text=key,background='pink',foreground='black')
                        break
                break
        
        if (check==False): # if the letter typed is not part of the keyword
            # Need some type of feedback later
            print("Error","This letter is not available.\nTry again")
            #messagebox.showerror("Error","This letter is not available.\nTry again")
        
        
    # This function starts the count-down timer 
    def start_timer(self):
        self.controller.start_timer()
    
    
    # This function displays a time (given in second) on the game view
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


    
def main():
    mygame=Game()
    mygame.master.mainloop()
    
if __name__ == "__main__": main()