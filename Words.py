import itertools

class Words:
    def __init__(self):
        self.three_words = {}
        self.four_words = {}
        self.five_words = {}
        self.six_words = {}
        
        # Create dictionary of 3-letter words
        file3 = open("3-letter words.txt")
        word = file3.readline()
        while len(word) > 0:
            word = file3.readline()[:3]
            key = ''.join(sorted(word))
            if key not in self.three_words:
                self.three_words[key] = {word}
            else:
                self.three_words[key].add(word)
        file3.close()
        
        # Create dictionary of 4-letter words
        file4 = open("4-letter words.txt")
        word = file4.readline()
        while len(word) > 0:
            word = file4.readline()[:4]
            key = ''.join(sorted(word))
            if key not in self.four_words:
                self.four_words[key] = {word}
            else:
                self.four_words[key].add(word)
        file4.close()
        
        # Create dictionary of 5-letter words
        file5 = open("5-letter words.txt")
        word = file5.readline()
        while len(word) > 0:
            word = file5.readline()[:5]
            key = ''.join(sorted(word))
            if key not in self.five_words:
                self.five_words[key] = {word}
            else:
                self.five_words[key].add(word)
        file5.close()

        # Create dictionary of 6-letter words
        file6 = open("6-letter words.txt")
        word = file6.readline()
        while len(word) > 0:
            word = file6.readline()[:6]
            key = ''.join(sorted(word))
            if key not in self.six_words:
                self.six_words[key] = {word}
            else:
                self.six_words[key].add(word)
        file6.close()
        
        self.allkeys = self.six_words.keys()

    def generate_words(self, word):
        all_words = {}
        all_words[3] = self.generate_n_letter_words(word, 3)
        all_words[4] = self.generate_n_letter_words(word, 4)
        all_words[5] = self.generate_n_letter_words(word, 5)
        all_words[6] = self.generate_n_letter_words(word, 6)
        return all_words
    
    def generate_n_letter_words(self, word, num_letters):
        x = itertools.combinations(word, num_letters)
        res = set()
        for s in x:
            temp = ''.join(sorted(s))
            if num_letters == 3:
                if temp in self.three_words:
                    res = res | self.three_words[temp]
            elif num_letters == 4:
                if temp in self.four_words:
                    res = res | self.four_words[temp]
            elif num_letters == 5:
                if temp in self.five_words:
                    res = res | self.five_words[temp]
            elif num_letters == 6:
                if temp in self.six_words:
                    res = res | self.six_words[temp]
        return sorted(res)
    
    def play(self):
        return 1


def main():
    example = Words()
    print(example.generate_words("houses"))
    # y = generate_n_letter_words("treads", 6)
    # for s in y:
    #     print(s)
    print("Done")
    
if __name__ == "__main__": main()
