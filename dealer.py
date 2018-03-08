from random import *

class Dealer:
    def init(self, deck):
        self.deck = deck

    def deal_card(self):
        return self.deck.pop()
        
    def shuffle_deck(self):
        shuffle(self.deck)