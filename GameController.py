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
    
    def get_letter(self):
        self.view.type_character

    def send_curKey(self):
        self.view.display_curKey(self.get_curKey())
        
    def play_word(self, word):
        word_score = self.model.play_word(word)
        if word_score > 0:
            self.increase_score(word_score)
        self.view.reset_input()
    
    def increase_score(self, word_score):
        self.score += word_score
        self.view.update_score()
        
    def increase_time(self, time):
        self.time_remaining += time
        self.view.display_time(self.time_remaining)
    
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