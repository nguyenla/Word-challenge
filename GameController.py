from GameModel import *
from GameGUI import Game
import time

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.score = 0
        self.time_remaining = 120
        self.view = Game()
        self.view.register_controller(self)
        self.send_curKey()
        
    def get_curKey(self):
        return self.model.curKey
    
    # TO-DO: Review this function. Uncertain where this is called
    def get_letter(self):
        self.view.type_character

    def send_curKey(self):
        self.view.display_curKey(self.get_curKey())
        
    def play_word(self, word):
        word_score = self.model.play_word(word)
        if word_score > 0:
            self.view.type_character(word)
            self.increase_score(word_score)
        elif word_score == 0: # replace later with other feedback
            print("Word has already been played.")
        else:
            print("Invalid word") # replace later with other feedback
        self.view.reset_input()
        return word_score
    
    # This function increases the score by the amount specified by word_score,
    # and then updates the score in the field
    def increase_score(self, word_score):
        self.score += word_score
        self.view.update_score()
        
    # This function increases the time remaining by the amount specified by the parameter time,
    # and then updates the time in the field
    def increase_time(self, time):
        self.time_remaining += time
        self.view.display_time(self.time_remaining)
    
    
    # TO-DO: Investigate a better way to do timer
    def start_timer(self):
        if self.time_remaining <= 0:
            self.view.display_time(-1)
        else:
            self.view.display_time(self.time_remaining)
            self.time_remaining -= 1
            self.view.master.after(1000, self.start_timer)

def main():
    newGame = GameController()
    #print(newGame.view.controller.get_curKey())
    newGame.send_curKey()
    newGame.view.master.mainloop()
   

if __name__ == "__main__": main()    