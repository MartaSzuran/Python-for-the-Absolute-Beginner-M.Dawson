# Simple pet with class
# presents classes attributes and static method

class Critter(object):
    """Virtual pet"""
    total = 0

    @staticmethod
    def status():
        print("\nTotal number of pets:", Critter.total)

    def __init__(self, name):
        print("New pet was born!")
        self.name = name
        Critter.total += 1


# main part
print("Getting access to class attribute Critter.total:", end= " ")
print(Critter.total)

# creating new pets
crit1 = Critter("pet 1")
crit2 = Critter("pet 2")
crit3 = Critter("pet 3")

Critter.status()

print("Getting access to class attribute through object:", end= " ")
print(crit1.total)


input("\n\nFor finish press Enter.")
