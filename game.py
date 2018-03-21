from cards import Cards
from dealer import Dealer
from player import Player
from rules import Rules
from random import *

rules = Rules()

end = 0
while end != 1:
    dealer = Dealer()
    player_one = Player()

    dealer.init(Cards.deck)
    player_one.init()

    dealer.shuffle_deck()

    # Deal two cards
    card = dealer.deal_card()
    player_one.take_card(card)
    card = dealer.deal_card()
    player_one.take_card(card)

    new = 1
    while new == 1:
        print(f'Hand: {" - ".join(player_one.hand)}')
        score = player_one.get_score()

        if score > 21:
            print(f'Final Score: {score} (Bust)')
            end, new = rules.quit()
            break
        elif score == 21:
            print(f'Final Score: {score} (Blackjack)')
            end, new = rules.quit()
            break

        print(f'Current Score: {score}')

        decision = input("Hit (H) or Stand (S)? ")
        if decision is 'H' or decision is 'h':
            card = dealer.deal_card()
            player_one.take_card(card)
        elif decision is 'S' or decision is 's':
            print(f'Final Score: {score}')
            quit = input("Do you want to quit? Yes(Y) or No(N)? ")
            end, new = rules.quit()
        else:
            end = 0



