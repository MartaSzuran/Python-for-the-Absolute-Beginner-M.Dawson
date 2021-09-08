# Pet with properties
# presents properties

class Critter(object):
    """Virtual pet"""
    def __init__(self, name):
        print("New pet was born!")
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Empty string cannot be pets name.")
        else:
            self.__name = new_name
            print("New name is set.")

    def talk(self):
        print("Hi! I am", self.name)


# main part
# creating an object
crit = Critter("Bob")
crit.talk()

print("\nMy pets name is: ", end="")
print(crit.name)

print("\nTry to change pets name to John...")
crit.name = "John"

print("\nMy pets name is: ", end="")
print(crit.name)

print("\nTry to change pets name to empty string...")
crit.name = ""

print("\nMy pets name is:", end="")
print(crit.name)


input("\n\nFor finish press Enter.")
