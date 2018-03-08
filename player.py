from cards import Cards

cards = Cards()

class Player:
    def init(self):
        self.hand = []
        self.score = 0
    
    def take_card(self, card):
        self.hand.append(card)
        self.evaluate_score()
        
    def evaluate_score(self):
        score = 0
        for card in self.hand:
            number, suite = card.split('_')
            score += cards.scores[number]
        self.score = score
    
    def get_score(self):
        return self.score