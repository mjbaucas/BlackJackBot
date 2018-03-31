from cards import Cards

class Rules:
    def init(self):
        self.end = 0
        self.new = 0

    def quit(self):
        quit = input("Do you want to quit? Yes(Y) or No(N)? ")
        if quit is 'Y' or quit is 'y':
            self.end = 1
            self.new = 1
        elif quit is 'N' or quit is 'n':
            self.end = 0
            self.new = 0
        else:
            self.end = 0
            self.new = 0
        return self.end, self.new

    def dealHand(self, player_one, dealer):
        # Deal two cards to player
        card = dealer.deal_card()
        player_one.take_card(card)
        card = dealer.deal_card()
        player_one.take_card(card)

        # Deal two cards to dealer
        card = dealer.deal_card()
        dealer.take_card(card)
        card = dealer.deal_card()
        dealer.take_card(card)

    def clearHand(self, player_one, dealer):
        # Clear Hands
        player_one.hand = []
        player_one.aces = 0
        dealer.hand = []

        # If cards are running low reset the decks
        deck = Cards.deck
        # If a deck gets below 30 cards reset it
        if len(dealer.deck1) < 30:
            dealer.deck1 = deck[:]
            dealer.shuffle_deck()
        if len(dealer.deck2) < 30:
            dealer.deck2 = deck[:]
            dealer.shuffle_deck()
        if len(dealer.deck3) < 30:
            dealer.deck3 = deck[:]
            dealer.shuffle_deck()
        if len(dealer.deck4) < 30:
            dealer.deck4 = deck[:]
            dealer.shuffle_deck()

    def whowon(self, player_one, dealer):
        if player_one.get_score() > 21:
            # Player bust
            print(f'You busted with a score of {player_one.get_score()}. The dealer wins!')
            player_one.update_basiclosses()
            player_one.units -= 1
            return 0
        elif player_one.get_score() == 21 and dealer.get_score() != 21:
            # Player Blacjack!
            print(f'You won by getting Blackjack!')
            player_one.update_basicwins()
            player_one.units += 1.5
            player_one.blackjacks += 1
            return 1
        elif player_one.get_score() <= 21 and dealer.get_score() > 21:
            # Dealer busts
            print(f'The dealer busted with a score of {dealer.get_score()}! You win!')
            player_one.update_basicwins()
            player_one.units += 1
            return 1
        elif dealer.get_score() <= 21 and dealer.get_score() > player_one.get_score():
            # Dealer wins
            print(f'The dealer wins!')
            player_one.units -= 1
            player_one.update_basiclosses()
            return 0
        elif player_one.get_score() <= 21 and player_one.get_score() > dealer.get_score():
            # Player wins
            print(f'Congratulations! You win!')
            player_one.update_basicwins()
            player_one.units += 1
            return 1
        elif player_one.get_score() == dealer.get_score():
            # Its a tie
            print(f'The result is a push (tie).')
            player_one.update_basicties()
            return 2
