# Card game
# Shows inheritance - methods shadow

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


class Unprintable_Card(Card):
    """Card which will not be shown (face_down) while printing"""
    def __str__(self):
        return "<secret>"


class Positionable_Card(Card):
    """Card which can be face_up or face_down"""
    def __init__(self, rank, suit, face_up=True):
        # super() == superclass
        super(Positionable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Positionable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

# main
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Show objects Card class:")
print(card1)

print("Show objects Unprintable_Card class:")
print(card2)

print("Show objects Positionable_Card class:")
print(card3)

print("State flip to object Positionable_Card (face_up / face_down).")
card3.flip()

print("Show objects Positionable_Card class:")
print(card3)

input("\nFor finish press Enter.")
