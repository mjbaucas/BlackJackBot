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
