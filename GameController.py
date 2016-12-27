from GameModel import *
from GameGUI import Game
import time

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.view = Game()
        self.score = 0
        self.time_remaining = 120
        self.view.register_controller(self)
        self.view.create_labels()
        self.send_curKey()
        
    # Return the current key of the game
    def get_curKey(self):
        return self.model.curKey

    # Display the current key of the game on the view
    def send_curKey(self):
        self.view.display_curKey(self.get_curKey())
        
    # This function plays a word to the model
    def play_word(self, word):
        position = 0 # the position of the word in the corresponding sorted list, if it is in the list
        if len(word) == 3:
            if word in self.model.three_fixed:
                position = self.model.three_fixed.index(word)
        elif len(word) == 4:
            if word in self.model.four_fixed:
                position = self.model.four_fixed.index(word)
        elif len(word) == 5:
            if word in self.model.five_fixed:
                position = self.model.five_fixed.index(word)
        elif len(word) == 6:
            if word in self.model.six_fixed:
                position = self.model.six_fixed.index(word)
        
        word_score = self.model.play_word(word)
        if word_score > 0:
            print(self.model.three)
            self.view.type_character(word, position)
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
    
    # This function generates and displays a new key for the game
    def get_new_key(self):
        self.model.get_next_key() 
        self.view.reset_input() # reset the input area on the game view
        self.send_curKey() # display the new key on the game view
        self.view.create_labels() # reset the labels that hold the words formed
        

def main():
    newGame = GameController()
    newGame.send_curKey()
    newGame.view.master.mainloop()
   

if __name__ == "__main__": main()    