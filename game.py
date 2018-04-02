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
# Do basic strategy game if basic set to 1, do training if training set to 1
basic = 0
training = 1
# Training Loop

if training == 1:
    for x in range(0, 10000):
        rules.dealHand(player_one, dealer)

        new = 1
        while new == 1:
            print(f'Player\'s Hand: {" - ".join(player_one.hand)}')
            print(f'Dealer\'s Hand: {dealer.hand[0]}')

            # Check players score for bust or blackjack
            if player_one.get_score() > 21:
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break
            elif player_one.get_score() == 21:
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break

            # Check if dealer was dealt black jack, if so game is over
            if dealer.get_score() == 21:
                print(f'Dealer\'s Hand: {" - ".join(dealer.hand)}')
                print(f'Dealer was dealt Blackjack! Better luck next time.')
                # end, new = rules.quit()
                break



            print(f'Player\'s Current Score: {player_one.get_score()}')
            print(f'Dealer\'s One Card Score: {dealer.get_one_card_score()}')

            # Let player decide what to do
            if robot == 0:
                decision = input("Hit (H) or Stand (S)? ")
            elif robot == 1:
                decision = player_one.QLearning_strategy(dealer)

            if decision is 'H' or decision is 'h':
                player_one.hit(dealer)
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
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break
            else:
                end = 0

        rules.clearHand(player_one, dealer)

    print(f' {player_one.QSoftStrategy}')
    print(f' {player_one.QStrategy}')

    player_one.basiclosses = 0
    player_one.basicwins = 0
    player_one.basicties = 0
    player_one.blackjacks = 0
    player_one.units = 0
    # Trained Strategy Loop
    for x in range(0, 10000):
        rules.dealHand(player_one, dealer)

        new = 1
        while new == 1:
            print(f'Player\'s Hand: {" - ".join(player_one.hand)}')
            print(f'Dealer\'s Hand: {dealer.hand[0]}')

            # Check players score for bust or blackjack
            if player_one.get_score() > 21:
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break
            elif player_one.get_score() == 21:
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break

            # Check if dealer was dealt black jack, if so game is over
            if dealer.get_score() == 21:
                print(f'Dealer\'s Hand: {" - ".join(dealer.hand)}')
                print(f'Dealer was dealt Blackjack! Better luck next time.')
                rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break

            print(f'Player\'s Current Score: {player_one.get_score()}')
            print(f'Dealer\'s One Card Score: {dealer.get_one_card_score()}')

            # Let player decide what to do
            if robot == 0:
                decision = input("Hit (H) or Stand (S)? ")
            elif robot == 1:
                decision = player_one.QLearning_strategy(dealer)

            if decision is 'H' or decision is 'h':
                player_one.hit(dealer)
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
                winner = rules.whowon(player_one, dealer)
                player_one.updateQStrategy(dealer, winner)
                # end, new = rules.quit()
                break
            else:
                end = 0

        rules.clearHand(player_one, dealer)

    print(f'Record: {player_one.basicwins}-{player_one.basiclosses}-{player_one.basicties}')
    print(f'Winning Pct: {round((player_one.basicwins/(player_one.basicwins + player_one.basiclosses))*100, 2)}%')
    print(f'Player Units: {player_one.units}')
    print(f'Player Blackjacks: {player_one.blackjacks}')

if (basic == 1):
    # Basic Strategy Loop
    for x in range (0, 1000000):
        rules.dealHand(player_one, dealer)

        new = 1
        while new == 1:
            print(f'Player\'s Hand: {" - ".join(player_one.hand)}')
            print(f'Dealer\'s Hand: {dealer.hand[0]}')

            # Check players score for bust or blackjack
            if player_one.get_score() > 21:
                rules.whowon(player_one, dealer)
                #end, new = rules.quit()
                break
            elif player_one.get_score() == 21:
                rules.whowon(player_one, dealer)
                #end, new = rules.quit()
                break


            # Check if dealer was dealt black jack, if so game is over
            if dealer.get_score() == 21:
                print(f'Dealer\'s Hand: {" - ".join(dealer.hand)}')
                print(f'Dealer was dealt Blackjack! Better luck next time.')
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
                player_one.hit(dealer)
            elif decision is 'S' or decision is 's':
                print(f'Player Stands.')
                print(f'Player\'s Final Score: {player_one.get_score()}')
                # Let the dealer play here and then compare
                print(f'The dealer will now play. \nThe dealer must hit if score is lower than 17.')
                print(f'Dealer\'s Current Hand: {" - ".join(dealer.hand)}')
                print(f'Dealer\'s Current Score: {dealer.get_score()}')
                while dealer.get_score() < 17:
                    # Dealer must hit if score is less than 17
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

