from GameModel import *
from GameGUI import Game

class GameController:
    def __init__(self):
        self.model = GameModel()
        self.score = 0
        self.view = Game()
        self.view.register_controller(self)
        
    def get_curKey(self):
        return self.model.curKey
    
    def send_curKey(self):
        self.view.display_curKey(self.get_curKey())
        
    def increase_score(self):
        self.score += 10
        self.view.update_score()
        
    

def main():
    newGame = GameController()
    #print(newGame.view.controller.get_curKey())
    newGame.send_curKey()
    newGame.view.master.mainloop()
   

if __name__ == "__main__": main()    
    