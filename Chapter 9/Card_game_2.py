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

class Deck(Hand):
    """Card deck."""
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("I cant deal out anymore. No more cards in deck!")


# main
deck1 = Deck()
print("I have created new deck.")
print("Deck:")
print(deck1)

deck1.populate()
print("I have added 52 cards to deck.")
print("Deck:")
print(deck1)

deck1.shuffle()
print("I have shuffled deck.")
print("Deck:")
print(deck1)

# creates two hands
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck1.deal(hands, per_hand=5)

print("I have deck out 5 card each.")
print("My hand:")
print(my_hand)
print("Your hand:")
print(your_hand)
print("Deck:")
print(deck1)

deck1.clear()
print("I have deleted deck content.")

print("Deck:", deck1)


input("\nFor finish press Enter.")
