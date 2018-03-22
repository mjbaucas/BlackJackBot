from random import *
from cards import Cards

cards = Cards()

class Dealer:
    def init(self, deck):
        self.deck = deck
        self.hand = []
        self.score = 0

    def deal_card(self):
        return self.deck.pop()
        
    def shuffle_deck(self):
        shuffle(self.deck)

    def take_card(self, card):
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            number, suite = card.split('_')
            score += cards.scores[number]
            if number == 'A':
                aces += 1
        if score > 21 and aces > 0:
            while aces > 0 and score > 21:
                score -= 10
                aces -= 1

        self.score = score

    def get_score(self):
        return self.score