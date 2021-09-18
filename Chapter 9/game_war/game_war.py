# Game war
# Challenge 2 chapter 9

import cards
import games


class WarCard(cards.Card):
    """War game cards."""
    @property
    def value(self):
        v = WarCard.RANKS.index(self.rank) + 1
        if v == 1:
            v = 14
        return v


class WarDeck(cards.Deck):
    """War game deck."""
    def populate(self):
        for suit in WarCard.SUITS:
            for rank in WarCard.RANKS:
                self.cards.append(WarCard(rank, suit))


class WarHand(cards.Hand):
    """Hand."""
    def __init__(self, name):
        super(WarHand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(WarHand, self).__str__()
        return rep

    @property
    def score(self):
        for card in self.cards:
            score = card.value
            return score


class WarGame(object):
    """War game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = WarHand(name)
            self.players.append(player)

        self.deck = WarDeck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # deal first cards to every player
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            print(player)

        highest_score = 0
        winners = []
        for player in self.players:
            print(player.score)

        for player in self.players:
            # print(player.score)
            if player.score > highest_score:
                highest_score = player.score
            print(highest_score)

        for player in self.players:
            score = player.score
            if score == highest_score:
                winners.append(player.name)

        for winner in winners:
            print(winner, "wins.")

        # erase every player cards
        for player in self.players:
            player.clear()


def main():
    print("\t\tWelcome in game 'WAR'!")

    names = []
    number = games.ask_number("Give me number of players (1-7): ", low=1, high=8)
    for i in range(number):
        name = input("Player name is: ")
        names.append(name)
    print()

    game = WarGame(names)
    game.play()

print()
main()


input("\n\nPress Enter to exit.")
