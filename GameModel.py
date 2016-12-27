from Words import Words
from random import randint

class GameModel:
    def __init__(self):
        self.words = Words()
        
        # All possible keys to use
        self.allKeys = []
        for k in self.words.allkeys:
            dic = self.words.generate_words(k)
            max_score_possible = len(dic[3])*30 + len(dic[4])*40 + len(dic[5])*50 + len(dic[6])*60
            if max_score_possible > 300:
                self.allKeys.append(k)
        
        # get a random key word to start the game
        rand = randint(0, len(self.allKeys) -1)
        self.curKey = self.allKeys[rand]
        self.allKeys.remove(self.curKey)
        
        self.dict = self.words.generate_words(self.curKey)
        
        # lists of words that can be generated from the current key
        self.three = self.dict[3]
        self.four = self.dict[4]
        self.five = self.dict[5]
        self.six = self.dict[6]
        
        # these copies are never modified
        self.three_fixed = list(self.dict[3])
        self.four_fixed = list(self.dict[4])
        self.five_fixed = list(self.dict[5])
        self.six_fixed = list(self.dict[6])
        
        # list of words that have already been played
        self.played = [] 
        
        # total number of words that can be generated
        self.num_words = len(self.dict[3]) + len(self.dict[4]) + len(self.dict[5]) + len(self.dict[6])
        
    # This method gets the next key word for the game model
    def get_next_key(self):
        n = len(self.allKeys)
        rand = randint(0,n-1)
        key = self.allKeys[rand]
        self.allKeys.remove(key)
        self.curKey = key
        
        self.dict = self.words.generate_words(self.curKey)
        self.three = self.dict[3]
        self.four = self.dict[4]
        self.five = self.dict[5]
        self.six = self.dict[6]
        
        self.three_fixed = list(self.dict[3])
        self.four_fixed = list(self.dict[4])
        self.five_fixed = list(self.dict[5])
        self.six_fixed = list(self.dict[6])
        
        self.num_words = len(self.dict[3]) + len(self.dict[4]) + len(self.dict[5]) + len(self.dict[6])
        self.played = []
    
    # If the word is valid and if it has not been played yet, return the score
    # Return 0 if the word is valid but it has already been played
    # Return -1 if the word is not valid
    def play_word(self, word):
        length = len(word)
        if not self.is_valid(word):
            return -1
        elif word in self.played:
            return 0
        
        elif length == 3:
            if word in self.three:
                self.played.append(word)
                self.three.remove(word)
                return 30
        elif length == 4:
            if word in self.four:
                self.played.append(word)
                self.four.remove(word)
                return 40
        elif length == 5:
            if word in self.five:
                self.played.append(word)
                self.five.remove(word)
                return 50
        elif length == 6:
            if word in self.six:
                self.played.append(word)
                self.six.remove(word)
                return 60
        return - 1
    
    # Check if a word can be formed by the letters from the key
    def is_valid(self, word):
        temp = sorted(self.curKey)
        for char in sorted(word):
            if not char in temp:
                return False
            else:
                temp.remove(char)
        return True
    
    def printAll(self):
        print(self.three)
        print(self.four)
        print(self.five)
        print(self.six)

def main():
    game = GameModel()
    print("Let the Word Challenge begin!")
    print("Type all the words that can be formed with the letters in the word: " + game.curKey)
    total = game.num_words
    found = 0
    w = input("Type in a word:")
    while True:
        m = game.play_word(w)
        if m == 0:
            #game.printAll()
            w = input(w + " has already been played. Type in another word:")
        elif m > 1:
            #game.printAll()
            found += 1
            if found > 1:
                game.get_next_key()
                found = 0
                total = game.num_words
                #print("Your score is: " + str(game.score))
                w = input("Good job! Next game: Type all the words that can be formed with the letters in the word: " + game.curKey)
            else:
                w = input("Correct! You have found " + str(found) + " out of " + str(total) + " words. Type in another word:") 
        else:
            #game.printAll()
            w = input(w + " is not a valid word. Type in another word:") 
    
    
if __name__ == "__main__": main()