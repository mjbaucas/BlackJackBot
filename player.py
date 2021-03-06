from cards import Cards
from random import *

cards = Cards()

class Player:
    def init(self):
        self.hand = []
        self.score = 0
        self.aces = 0
        self.basicwins = 0
        self.basiclosses = 0
        self.basicties = 0
        self.units = 100
        self.blackjacks = 0

        # Key is player_dealer scores, value is hit or stand
        self.strategy = {'20_2': 'S', '20_3': 'S', '20_4': 'S', '20_5': 'S', '20_6': 'S', '20_7': 'S', '20_8': 'S',
                            '20_9': 'S', '20_10': 'S', '20_11': 'S',
                        '19_2': 'S', '19_3': 'S', '19_4': 'S', '19_5': 'S', '19_6': 'S', '19_7': 'S', '19_8': 'S',
                            '19_9': 'S', '19_10': 'S', '19_11': 'S',
                        '18_2': 'S', '18_3': 'S', '18_4': 'S', '18_5': 'S', '18_6': 'S', '18_7': 'S', '18_8': 'S',
                            '18_9': 'S', '18_10': 'S', '18_11': 'S',
                        '17_2': 'S', '17_3': 'S', '17_4': 'S', '17_5': 'S', '17_6': 'S', '17_7': 'S', '17_8': 'S',
                            '17_9': 'S', '17_10': 'S', '17_11': 'S',
                        '16_2': 'S', '16_3': 'S', '16_4': 'S', '16_5': 'S', '16_6': 'S', '16_7': 'H', '16_8': 'H',
                            '16_9': 'H', '16_10': 'H', '16_11': 'H',
                        '15_2': 'S', '15_3': 'S', '15_4': 'S', '15_5': 'S', '15_6': 'S', '15_7': 'H', '15_8': 'H',
                            '15_9': 'H', '15_10': 'H', '15_11': 'H',
                        '14_2': 'S', '14_3': 'S', '14_4': 'S', '14_5': 'S', '14_6': 'S', '14_7': 'H', '14_8': 'H',
                            '14_9': 'H', '14_10': 'H', '14_11': 'H',
                        '13_2': 'S', '13_3': 'S', '13_4': 'S', '13_5': 'S', '13_6': 'S', '13_7': 'H', '13_8': 'H',
                            '13_9': 'H', '13_10': 'H', '13_11': 'H',
                        '12_2': 'H', '12_3': 'H', '12_4': 'S', '12_5': 'S', '12_6': 'S', '12_7': 'H', '12_8': 'H',
                            '12_9': 'H', '12_10': 'H', '12_11': 'H',
                        '11_2': 'H', '11_3': 'H', '11_4': 'H', '11_5': 'H', '11_6': 'H', '11_7': 'H', '11_8': 'H',
                            '11_9': 'H', '11_10': 'H', '11_11': 'H',
                        '10_2': 'H', '10_3': 'H', '10_4': 'H', '10_5': 'H', '10_6': 'H', '10_7': 'H', '10_8': 'H',
                            '10_9': 'H', '10_10': 'H', '10_11': 'H',
                        '9_2': 'H', '9_3': 'H', '9_4': 'H', '9_5': 'H', '9_6': 'H', '9_7': 'H', '9_8': 'H', '9_9': 'H',
                            '9_10': 'H', '9_11': 'H',
                        '8_2': 'H', '8_3': 'H', '8_4': 'H', '8_5': 'H', '8_6': 'H', '8_7': 'H', '8_8': 'H', '8_9': 'H',
                            '8_10': 'H', '8_11': 'H',
                        '7_2': 'H', '7_3': 'H', '7_4': 'H', '7_5': 'H', '7_6': 'H', '7_7': 'H', '7_8': 'H', '7_9': 'H',
                            '7_10': 'H', '7_11': 'H',
                        '6_2': 'H', '6_3': 'H', '6_4': 'H', '6_5': 'H', '6_6': 'H', '6_7': 'H', '6_8': 'H', '6_9': 'H',
                            '6_10': 'H', '6_11': 'H',
                        '5_2': 'H', '5_3': 'H', '5_4': 'H', '5_5': 'H', '5_6': 'H', '5_7': 'H', '5_8': 'H', '5_9': 'H',
                            '5_10': 'H', '5_11': 'H',
                        '4_2': 'H', '4_3': 'H', '4_4': 'H', '4_5': 'H', '4_6': 'H', '4_7': 'H', '4_8': 'H', '4_9': 'H',
                            '4_10': 'H', '4_11': 'H',
                    }

        self.softstrategy = {'20_2': 'S', '20_3': 'S', '20_4': 'S', '20_5': 'S', '20_6': 'S', '20_7': 'S', '20_8': 'S',
                                '20_9': 'S', '20_10': 'S', '20_11': 'S',
                             '19_2': 'S', '19_3': 'S', '19_4': 'S', '19_5': 'S', '19_6': 'S', '19_7': 'S', '19_8': 'S',
                                '19_9': 'S', '19_10': 'S', '19_11': 'S',
                             '18_2': 'S', '18_3': 'S', '18_4': 'S', '18_5': 'S', '18_6': 'S', '18_7': 'S', '18_8': 'S',
                                '18_9': 'H', '18_10': 'H', '18_11': 'H',
                             '17_2': 'H', '17_3': 'H', '17_4': 'H', '17_5': 'H', '17_6': 'H', '17_7': 'H', '17_8': 'H',
                                '17_9': 'H', '17_10': 'H', '17_11': 'H',
                             '16_2': 'H', '16_3': 'H', '16_4': 'H', '16_5': 'H', '16_6': 'S', '16_7': 'H', '16_8': 'H',
                                '16_9': 'H', '16_10': 'H', '16_11': 'H',
                             '15_2': 'H', '15_3': 'H', '15_4': 'H', '15_5': 'H', '15_6': 'H', '15_7': 'H', '15_8': 'H',
                                '15_9': 'H', '15_10': 'H', '15_11': 'H',
                             '14_2': 'H', '14_3': 'H', '14_4': 'H', '14_5': 'H', '14_6': 'H', '14_7': 'H', '14_8': 'H',
                                '14_9': 'H', '14_10': 'H', '14_11': 'H',
                             '13_2': 'H', '13_3': 'H', '13_4': 'H', '13_5': 'H', '13_6': 'H', '13_7': 'H', '13_8': 'H',
                                '13_9': 'H', '13_10': 'H', '13_11': 'H'
                             }

        self.QStrategy= {}
        self.QSoftStrategy = {}
    
    def take_card(self, card):
        self.hand.append(card)
        self.update_score()
        
    def update_score(self):
        score = 0
        for card in self.hand:
            number, suit = card.split('_')
            score += cards.scores[number]
            if number == 'A':
                self.aces += 1
        if score > 21 and self.aces > 0:
            while self.aces > 0 and score > 21:
                score -= 10
                self.aces -= 1

        self.score = score
    
    def get_score(self):
        return self.score

    def hit(self, dealer):
        print(f'Player Hits.')
        card = dealer.deal_card()
        self.take_card(card)

    def randomhit(self, dealer):
        hit = randint(0, 1)
        if hit == 1:
            decision = 'H'
        else:
            decision = 'S'
        return decision

    def basic_strategy(self, player_one, dealer):
        combined = str(player_one.get_score()) + "_" + str(dealer.get_one_card_score())
        if self.aces >= 1 and len(self.hand) == 2 and self.score > 12:
            decision = self.softstrategy[combined]
        else:
            decision = self.strategy[combined]
        return decision

    def QLearning_strategy(self, dealer):
        combined = str(self.get_score()) + "_" + str(dealer.get_one_card_score())
        if self.aces >= 1 and len(self.hand) == 2 and self.score > 12:
            if combined in self.QSoftStrategy:
                if self.QSoftStrategy[combined] > 0:
                    decision = 'S'
                elif self.QSoftStrategy[combined] < 0:
                    decision = 'H'
                else:
                    decision = self.randomhit(dealer)
            else:
                decision = self.randomhit(dealer)
        else:
            if combined in self.QStrategy:
                if self.QStrategy[combined] > 0:
                    decision = 'S'
                elif self.QStrategy[combined] < 0:
                    decision = 'H'
                else:
                    decision = self.randomhit(dealer)
            else:
                decision = self.randomhit(dealer)
        return decision

    def updateQStrategy(self, dealer, winner):
        # Update QStrategy dictionaries
        self.hand.pop(-1)
        combined = str(self.get_score()) + "_" + str(dealer.get_one_card_score())
        if self.aces >= 1 and len(self.hand) == 2 and self.score > 12:
            if combined in self.QSoftStrategy:
                self.updateQSoftStrategyDict(combined, winner)
            else:
                self.QSoftStrategy[combined] = 0
                self.updateQSoftStrategyDict(combined, winner)
        else:
            if combined in self.QStrategy:
                self.updateQStrategyDict(combined, winner)
            else:
                self.QStrategy[combined] = 0
                self.updateQStrategyDict(combined, winner)

    def updateQStrategyDict(self, combined, winner):
        if winner == 1:
            self.QStrategy[combined] += 1
        elif winner == 0:
            self.QStrategy[combined] -= 1

    def updateQSoftStrategyDict(self, combined, winner):
        if winner == 1:
            self.QSoftStrategy[combined] += 1
        elif winner == 0:
            self.QSoftStrategy[combined] -= 1

    def update_basicwins(self):
        self.basicwins += 1

    def update_basiclosses(self):
        self.basiclosses += 1

    def update_basicties(self):
        self.basicties += 1
