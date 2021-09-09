# Pet caregiver
# Virtual pet, user can choose amount of food

class Critter(object):
    """Virtual pet"""

    def __init__(self, name, hunger=0, boredom=0):
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

    def eat(self):
        amount_of_food = None
        food = 0
        while amount_of_food != "0":
            amount_of_food = input("\nHow many food you would like to give to me from 1 to 3 units?: ")
            if amount_of_food == "1":
                print("\nYummy, yummy. Thank you.")
                food = 4
                break
            elif amount_of_food == "2":
                print("\nYummy, yummy. Thank you. Now I have much more energy!!!")
                food = 5
                break
            elif amount_of_food == "3":
                print("\nYou want to make me fat human... all right I will eat it all any way!")
                food = 6
                break
            else:
                print("\nYou can choose number from 1 to 3.")
                amount_of_food = input("\nHow many food you would like to give to me from 1 to 3 units?: ")

        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        minutes_of_playing = None
        fun = 0
        while minutes_of_playing != "0":
            minutes_of_playing = int(input("\nHow long would you like to play with me from 5 to 30 minutes?: "))
            if 5 <= minutes_of_playing <= 10:
                print("\nHooray")
                fun = 4
                break
            elif 11 <= minutes_of_playing <= 20:
                print("\nLove to playing with you!")
                fun = 5
                break
            elif 21 <= minutes_of_playing <= 30:
                print("\nPlaying with you is my dreams come true...!")
                fun = 6
                break
            else:
                print("\nYou can choose number from 5 to 30.")
                minutes_of_playing = int(input("\nHow long would you like to play with me from 5 to 30 minutes?: "))

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
        Pet caregiver 2
        
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
