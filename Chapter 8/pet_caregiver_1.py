# Pet caregiver
# Virtual pet, which you need to give care

class Critter(object):
    """Virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        print("New pet was born!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "pleased"
        elif 11 <= unhappiness <= 15:
            m = "jumpy"
        else:
            m = "angry"
        return m

    def talk(self):
        print("Hi! I am", self.name, "and I am", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Yummy, yummy. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Hooray")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

def main():
    crit_name = input("How you want to call your new pet?: ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        ("""
        Pet caregiver
        
        0 - end program
        1 - listen to your pet
        2 - feed your pet
        3 - play with your pet
        """)

        choice = input("You choose: ")
        print()

        # end program
        if choice == "0":
            print("Goodbye.")

        # listen to your pet
        elif choice == "1":
            crit.talk()

        # feed your pet
        elif choice == "2":
            crit.eat()

        # play with your pet
        elif choice == "3":
            crit.play()

        # unknown choice
        else:
            print("\nSorry", choice, "is invalid.")

main()
input("\n\nFor finish press Enter.")
