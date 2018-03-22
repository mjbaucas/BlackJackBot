from cards import Cards

cards = Cards()

class Player:
    def init(self):
        self.hand = []
        self.score = 0
    
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
        if score > 21 and aces > 0:
            while aces > 0 and score > 21:
                score -= 10
                aces -= 1

        self.score = score
    
    def get_score(self):
        return self.score

    def basic_strategy(self, player_one, dealer):
        if dealer.get_score() < 10:
            decision = 's'
        elif dealer.get_score() >= 10:
            decision = 'h'
        return  decision