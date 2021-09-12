# Blackjack
# 1 - 7 players rivalry with dealer

import cards
import games


class BJ_Card(cards.Card):
    """Blackjack card."""
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_Deck(cards.Deck):
    """Blackjack deck."""
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))


class BJ_Hand(cards.Hand):
    """Hand in blackjack."""
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if card in hand has value None, the total sum is None too
        for card in self.cards:
            if not card.value:
                return None

        # sum cards value, A is 1
        t = 0
        for card in self.cards:
            t += card.value

        # check if hand has got A
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand has got A and the sum is low enough
        # treat A as 11
        if contains_ace and t <= 11:
            # add just 10, becouse we already added 1 for A earlier
            t += 10

        return t

    # method use like is_on / is_off, which return true/false can be write like one above
    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """Blackjack player."""
    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want to take card? (Y/N): ")
        return response == "Y"

    def bust(self):
        print(self.name, "has bust.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins")

    def push(self):
        print(self.name, "ties.")


class BJ_Dealer(BJ_Hand):
    """Blackjack dealer."""
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "has bust.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """Blackjack game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        # deal first cards to every player
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()   # hide first dealer card
        for player in self.players:
            print(player)
        print(self.dealer)

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()   # show first dealers card

        if not self.still_playing:
            # because every player is busted, show only dealers hand
            print(self.dealer)
        else:
            # give additional cards
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # players wins how is still playing
                for player in self.still_playing:
                    player.win()
            else:
                # compare every player points who is still in game
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # erase every player cards
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWelcome in game 'Blackjack'!")

    names = []
    number = games.ask_number("Give me number of players (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("Player name is: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again?: ")


main()
input("\n\nFor finish press Enter.")
