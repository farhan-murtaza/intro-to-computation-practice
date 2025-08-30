import glob
import os
import pprint
print(os.getcwd())

# os.chdir('os-test')
print(os.listdir())

print(glob.glob('*.*'))

# os.rename()

file_sizes = []

for dir_path, dirs, files in os.walk("."):
    print("Running in: ", os.path.join(dir_path))

    for f in files:
        file_full_path = os.path.join(dir_path, f)
        file_size = os.path.getsize(file_full_path)

        file_sizes.append((file_full_path, file_size))
    

    print("")

# pprint.pprint(file_sizes)

file_sizes.sort(key=lambda x: x[1], reverse=True)
# pprint.pprint(file_sizes[:10])


filtered = filter(lambda x: x[1] > 1024 * 1024, file_sizes)
for f in filtered:
    print(f)




##------------------------------------------------------------------------------
# ---------------------------- Card and Decks ----------------------------------
##------------------------------------------------------------------------------


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def __str__(self):
        return str(self.val) + " of " + self.suit
    

class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Hearts", "Diamonds", "Clubs"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))
    
    def __str__(self):
        ret = ""
        for c in self.cards:
            ret += str(c) + "\n"
        return ret
    

c1 = Card("Hearts", 5)

print(c1)

d = Deck()
print(d)



import random

def shuffle(self):
    for i in range(0, len(self.cards)):
        r = random.randint(0, i)            # find another  number
        self.cards[i], self.cards[r] = self.cards[r], self.cards[i]     #swap


Deck.shuffle = shuffle

d.shuffle()
print(d)


def draw(self):
    r = random.randint(0 , len(self.cards))
    c = self.cards.pop(r)
    return c

Deck.draw = draw

c = d.draw()

print("----")
print(c)
