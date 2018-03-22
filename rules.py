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

    def whowon(self, player_one, dealer):
        if player_one.get_score() > 21:
            # Player bust
            print(f'You busted with a score of {player_one.get_score()}. The dealer wins!')
        elif player_one.get_score() == 21 and dealer.get_score() != 21:
            # Player Blacjack!
            print(f'You won by getting Blackjack!')
        elif player_one.get_score() <= 21 and dealer.get_score() > 21:
            # Dealer busts
            print(f'The dealer busted with a score of {dealer.get_score()}! You win!')
        elif dealer.get_score() <= 21 and dealer.get_score() > player_one.get_score():
            # Dealer wins
            print(f'The dealer wins!')
        elif player_one.get_score() <= 21 and player_one.get_score() > dealer.get_score():
            # Player wins
            print(f'Congratulations! You win!')
        elif player_one.get_score() == dealer.get_score():
            # Its a tie
            print(f'The result is a push (tie).')
