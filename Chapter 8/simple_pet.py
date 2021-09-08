# Simple pet
# creating simple class and object

class Critter(object):
    """Virtual pet"""
    def talk(self):
        print("Hi! I am an example of Critter class.")


# main part
crit = Critter()
crit.talk()

input("\n\nFor finish press Enter.")
