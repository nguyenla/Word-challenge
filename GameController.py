from GameModel import *
from GameGUI import GameMainView
from GameStartView import *
from GameEndView import *
from tkinter import Tk
import time
import pyglet

class GameController:
    def __init__(self):
        self.model = GameModel()
        root = Tk()
        root.minsize(width = 700, height = 600)
        root.title("Game")
        root.configure(background='#23B6C0')
        self.root = root
        
        self.view = GameStartView(root)
        self.score = 0
        self.partial_score = 0 # score earned from current key word
        self.time_remaining = 120
        self.view.register_controller(self)
        self.view.pack()
        
        
        # Play background music
        #self.music_player = pyglet.media.load('Lacrimosa.mp3')
        #self.music_player.play()

    def create_game(self):
        main_view = GameMainView(self.root)
        main_view.register_controller(self)
        self.view.destroy()
        self.view = main_view
        self.view.create_labels()
        self.send_curKey()
        self.view.pack()
    
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

        # Increase the score and the time remaining
        word_score = self.model.play_word(word)
        if word_score > 0:
            print(self.model.three)
            if word_score > 30:
                self.increase_time(word_score // 10)
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
        self.partial_score += word_score
        if word_score == 60: # if the 6-letter word is found, the player can get the next key word
            self.partial_score += 200
        self.view.update_score()

    # This function increases the time remaining by the amount specified by the parameter time,
    # and then updates the time in the field
    def increase_time(self, time):
        self.time_remaining += time
        self.view.display_time(self.time_remaining)


    # This function starts the timer
    def start_timer(self):
        if self.time_remaining <= 0:
            self.view.display_time(-1)
        else:
            self.view.display_time(self.time_remaining)
            self.time_remaining -= 1
            self.view.master.after(1000, self.start_timer)

    # This function generates and displays a new key for the game
    def get_new_key(self):
        # The player can only get a new key word after scoring at least 200 points from the current key word
        if self.partial_score >= 200:
            self.partial_score = 0
            self.model.get_next_key()
            self.view.reset_input() # reset the input area on the game view
            self.send_curKey() # display the new key on the game view
            self.view.create_labels() # reset the labels that hold the words formed
        else:
            print("You need to score 200 points from the current key word before you can get another key word.")
            print("Your current partial score is: " + str(self.partial_score))

    def end_game(self):
        print("The game ended.")
        end_view = GameEndView(self.view.master, self)
        self.view.destroy()
        self.view = end_view
        self.view.tkraise()

def main():
    newGame = GameController()
    newGame.view.mainloop()

if __name__ == "__main__": main()
