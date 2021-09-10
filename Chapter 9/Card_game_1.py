# Card game
# Shows objects combinations

class Card(object):
    """Card."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


# creating Hand class - will generate objects which are objects Card class collection
class Hand(object):
    """Hand - cards in players hand."""
    def __init__(self):
        # every single object is a list of objects
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


# main
card1 = Card(rank="A", suit="c")
print("Showing card object (class Card):")
print(card1)

card2 = Card(rank="2", suit="c")
card3 = Card(rank="3", suit="c")
card4 = Card(rank="4", suit="c")
card5 = Card(rank="5", suit="c")

print("\nShowing rest of objects one at the time:")
print(card2)
print(card3)
print(card4)
print(card5)

# group together objects (wrap together)
my_hand = Hand()
print("\nShowing my hand content before adding any cads:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)

print("\nShowing my hand content after adding 5 cads:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nGiving two first cards from my hand to your hand.")
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand)

my_hand.clear()
print("\nMy hand after erasing cards:")
print(my_hand)

input("\nFor finish press Enter.")
