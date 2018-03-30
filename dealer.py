from random import *
from cards import Cards

cards = Cards()

class Dealer:
    def init(self, deck1, deck2, deck3, deck4):
        self.deck1 = deck1
        self.deck2 = deck2
        self.deck3 = deck3
        self.deck4 = deck4
        self.hand = []
        self.score = 0
        self.one_card_score = 0

    def deal_card(self):
        # Need to take card from one of the four decks at random
        decknum = randint(1, 4)
        if decknum == 1:
            return self.deck1.pop()
        elif decknum == 2:
            return self.deck2.pop()
        elif decknum == 3:
            return self.deck3.pop()
        elif decknum == 4:
            return self.deck4.pop()

    def hit(self):
        # Dealer must hit if their score is less than 17
        card = self.deal_card()
        self.take_card(card)
        print(f'Dealer\'s Hand After Hit: {" - ".join(self.hand)}')
        print(f'Dealer\'s New Score After Hit: {self.get_score()}')
        
    def shuffle_deck(self):
        shuffle(self.deck1)
        shuffle(self.deck2)
        shuffle(self.deck3)
        shuffle(self.deck4)

    def reset_decks(self, deck1, deck2, deck3, deck4):
        self.deck1 = deck1
        self.deck2 = deck2
        self.deck3 = deck3
        self.deck4 = deck4

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