# Private pet
# presents variables and private methods

class Critter(object):
    """Virtual pet"""
    def __init__(self, name, mood):
        print("New pet was born!")
        self.name = name       # public attribute
        self.__mood = mood     # private attribute

    def talk(self):
        print("Hi! I am", self.name)
        print("In that moment I am", self.__mood, "\n")

    def __private_method(self):
        print("This is private method.")

    def public_method(self):
        print("This is public method.")
        self.__private_method()


# main part
# creating an object
crit = Critter(name="Bob", mood="happy")
crit.talk()
crit.public_method()

# getting access to private attribute through class
print(crit._Critter__mood)

# getting access to private method through class
crit._Critter__private_method()


input("\n\nFor finish press Enter.")
