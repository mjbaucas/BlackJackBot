from random import *
from cards import Cards

cards = Cards()

class Dealer:
    def init(self, deck):
        self.deck = deck
        self.hand = []
        self.score = 0
        self.one_card_score = 0

    def deal_card(self):
        return self.deck.pop()

    def return_card(self, card):
        return self.deck.append(card)
        
    def shuffle_deck(self):
        shuffle(self.deck)

    def take_card(self, card):
        self.hand.append(card)
        self.update_score()

    def update_score(self):
        score = 0
        aces = 0
        for card in self.hand:
            number, suit = card.split('_')
            score += cards.scores[number]
            if number == 'A':
                aces += 1
        if score > 17 and aces > 0:
            while aces > 0 and score > 21:
                score -= 10
                aces -= 1

        # This is the dealer's actual score
        self.score = score

        # This is the score we will display to the player
        number, suit = self.hand[0].split('_')
        self.one_card_score = cards.scores[number]

    def get_score(self):
        return self.score

    def get_one_card_score(self):
        return self.one_card_score