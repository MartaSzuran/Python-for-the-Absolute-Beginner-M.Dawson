# Simple pet with constructor
# presents constructors

class Critter(object):
    """Virtual pet"""
    def __init__(self):
        print("New pet was born!")

    def talk(self):
        print("Hi! I am an example of Critter class.")


# main part
# creating many objects
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()

input("\n\nFor finish press Enter.")
