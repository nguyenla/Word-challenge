from GameModel import *
from GameGUI import Game

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.score = 0
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
    
    def increase_score(self, word_score):
        self.score += word_score
        self.view.update_score()
    

def main():
    newGame = GameController()
    #print(newGame.view.controller.get_curKey())
    newGame.send_curKey()
    newGame.view.master.mainloop()
   

if __name__ == "__main__": main()    
    