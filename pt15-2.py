from random import shuffle

class Card():
    values = [None,None,"2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
    suits = ["Spade","Club","Heart","Diamond"]

    def __init__(self,v,s):
        self.value = v
        self.suit = s

    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            return self.suit < c2.suit
        return False

    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            return self.suit > c2.suit
        return False

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def draw(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player():
    def __init__(self,name):
        self.name = name
        self.card = None
        self.win = 0

class Game():
    def __init__(self):
        name1 = input("player name 1: ")
        name2 = input("player name 2: ")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()

    def print_winner(self, winner):
        print("{} wins in this round".format(winner.name))

    def print_draw(self,p1,p2):
        print("{} draws {}, {} draws {}".format(
        self.p1.name, self.p1.card, self.p2.name, self.p2.card))

    def winner(self,p1,p2):
        if p1.win > p2.win:
            return p1.name
        if p1.win < p2.win:
            return p2.name
        return "draw"

    def game(self):
        print("start war game")
        cards = self.deck.cards
        while len(cards) >= 2:
            e = input("q to quit, enter any key to start: ")
            if e == "q":
                break
            self.p1.card = self.deck.draw()
            self.p2.card = self.deck.draw()
            self.print_draw(self.p1,self.p2)
            if self.p1.card > self.p2.card:
                self.p1.win += 1
                self.print_winner(self.p1)
            else:
                self.p2.win += 1
                self.print_winner(self.p2)

        win = self.winner(self.p1, self.p2)
        print("{} win".format(win))

game = Game()
game.game()
