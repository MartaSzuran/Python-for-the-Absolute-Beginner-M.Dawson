# Game war
# Challenge 2 chapter 9

class Card(object):
    """War game cards."""
    SUITS = ["d", "s", "h", "c"]
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9",
             "10", "J", "Q", "K", "A"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        representation = self.rank + self.suit
        return representation

    @property
    def value(self):
        value = self.RANKS.index(self.rank) + 1
        return value


class Hand(object):
    """War game hand."""
    def __init__(self):
        self.cards = []

    def __str__(self):
        # if there are cards in card print it, else print empty hand
        if self.cards:
            representation = ""
            for card in self.cards:
                representation = str(card) + "\t"
        else:
            print("<empty>")
        return representation

    # adding card to cards
    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        # remove one card from cards list
        self.cards.remove(card)
        # add this card to hand
        other_hand.add(card)


class Deck(Hand):
    """War game deck."""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def mix_cards(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for i in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("End of cards.")


class Player(Hand):
    """War game player."""
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name

    def __str__(self):
        representation = self.name + "\t" + super(Player, self).__str__()
        return representation

    # need to add all values to cards in self.cards and then return score
    @property
    def score(self):
        for card in self.cards:
            score = card.value
        return score


class Game(object):
    """War game."""
    def __init__(self, names):
        self.players = []
        for name in names:
            player = Player(name)
            self.players.append(player)

        self.deck = Deck()
        self.deck.populate()
        self.deck.mix_cards()
        # print(self.players)

    def play(self):
        self.deck.deal(self.players, per_hand=1)
        for player in self.players:
            print(player)

        # for player in self.players:
            # print(player.score)

        winners = []
        highest_score = 0
        for player in self.players:
            if player.score > highest_score:
                highest_score = player.score
            # print(highest_score)

        for player in self.players:
            if player.score == highest_score:
                winners.append(player)
                # print(winners)

        if len(winners) >= 2:
            print("It is a tie!")
            print("The winners are: ")
            for winner in winners:
                print(winner)
        else:
            print("The winner is: ", winners[0])


def main():

    print("""\n\t\tWELCOME IN CARD GAME WAR!!\n\n""")
    names = []
    amount_of_players = input("Give me amount of players: ")
    while amount_of_players:
        if amount_of_players.isalpha():
            print("Input must be a number!")
            amount_of_players = input("Give me amount of players: ")
        elif int(amount_of_players) > 26:
            print("To many players, there can only be 26!")
            amount_of_players = input("Give me amount of players: ")
        elif int(amount_of_players) == 0:
            print("Too less players!")
            amount_of_players = input("Give me amount of players: ")
        else:
            for name in range(int(amount_of_players)):
                name = input("Give me players names: ")
                names.append(name)
            # print(names)
            break

    game = Game(names)
    game.play()

    response = input("Do you want to play again (y/n)?: \t")
    response = response.lower()
    while response:
        if response != "n" and response != "y":
            response = input("Do you want to play again (y/n)?: \t")
            response = response.lower()
        elif response == "y":
            main()
        else:
            print("Thank you!\n")
            input("To finish press Enter.")
            break


main()
