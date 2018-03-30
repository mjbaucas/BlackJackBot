from cards import Cards
from dealer import Dealer
from player import Player
from rules import Rules
from random import *

rules = Rules()
# Set robot to 0 if manually playing,
# Set robot to 1 if robot is playing
dealer = Dealer()
player_one = Player()

deck = Cards.deck
dealer.init(deck[:], deck[:], deck[:], deck[:])
player_one.init()

dealer.shuffle_deck()
robot = 1
end = 0

# Training Loop


# Trained Strategy Loop



# Basic Strategy Loop
for x in range (0,10000):
    rules.dealHand(player_one, dealer)

    new = 1
    while new == 1:
        print(f'Player\'s Hand: {" - ".join(player_one.hand)}')
        print(f'Dealer\'s Hand: {dealer.hand[0]}')

        # Check if dealer was dealt black jack, if so game is over
        if dealer.get_score() == 21:
            print(f'Dealer\'s Hand: {" - ".join(dealer.hand)}')
            print(f'Dealer was dealt Blackjack! Better luck next time.')
            #end, new = rules.quit()
            break

        # Check players score for bust or blackjack
        if player_one.get_score() > 21:
            rules.whowon(player_one, dealer)
            #end, new = rules.quit()
            break
        elif player_one.get_score() == 21:
            rules.whowon(player_one, dealer)
            #end, new = rules.quit()
            break

        print(f'Player\'s Current Score: {player_one.get_score()}')
        print(f'Dealer\'s One Card Score: {dealer.get_one_card_score()}')

        # Let player decide what to do
        if robot == 0:
            decision = input("Hit (H) or Stand (S)? ")
        elif robot == 1:
            decision = player_one.basic_strategy(player_one, dealer)

        if decision is 'H' or decision is 'h':
            print(f'Player Hits.')
            card = dealer.deal_card()
            player_one.take_card(card)
        elif decision is 'S' or decision is 's':
            print(f'Player Stands.')
            print(f'Player\'s Final Score: {player_one.get_score()}')
            # Let the dealer play here and then compare
            print(f'The dealer will now play. \nThe dealer must hit if score is lower than 17.')
            print(f'Dealer\'s Current Hand: {" - ".join(dealer.hand)}')
            print(f'Dealer\'s Current Score: {dealer.get_score()}')
            while dealer.get_score() < 17:
                # Dealer must hit if their score is less than 17
                dealer.hit()

            # Game is over. Find out who wins
            rules.whowon(player_one, dealer)
            #end, new = rules.quit()
            break
        else:
            end = 0

    rules.clearHand(player_one, dealer)

# Here we should print out a tally of win/loss ratio
print(f'Record: {player_one.basicwins}-{player_one.basiclosses}-{player_one.basicties}')
print(f'Winning Pct: {round((player_one.basicwins/(player_one.basicwins + player_one.basiclosses))*100, 2)}%')
print(f'Player Units: {player_one.units}')
print(f'Player Blackjacks: {player_one.blackjacks}')