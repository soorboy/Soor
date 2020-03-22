# def Hello_World():
#   print("Hello World!")
#   print();
# 
# 
# Hello_World()

import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{}-{}".format(self.value, self.suit))


# card = Card("Card", 6)
# card.show()

class Deck:
    def __init__ (self):
        self.cards = []
        self.build()

    def conv(self, v):
        switcher ={
            14: 'A',
            10: 'T',
            11: 'J',
            12: 'Q',
            13: 'K'
            }
        return switcher.get(v,v)
    
    def build(self):
        for s in ["S", "H", "C", "D"]:
            for v in range (14, 1, -1):
                v2 = self.conv(v)
                self.cards.append(Card(s,v2))

    def show(self):
        for c in self.cards:
            c.show()

deck = Deck()
deck.show()
