# Simple pet with attribute
# presents attributes and access to them

class Critter(object):
    """Virtual pet"""
    def __init__(self, name):
        print("New pet was born!")
        self.name = name

    # if I use print(crit1) I will get <__main__.Critter object at 0x00A0BA90>
    # so we have to use __str__() method to make representation for that object using string
    # like:
    # Object Critter class
    # name: Bob
    def __str__(self):
        rep = "Object Critter class\n"
        rep += "name: " + self.name + "\n"
        return rep

    def talk(self):
        print("Hi! I am", self.name, "\n")


# main part
crit1 = Critter("Bob")
crit1.talk()

crit2 = Critter("Rex")
crit2.talk()

print("View crit1 object:")
print(crit1)

print("Direct view of crit1.name attribute:")
print(crit1.name)

input("\n\nFor finish press Enter.")
