# Virtual farm
# creating many objects
# players is taking care of all of them
# random hunger nad boredom for every new pet

import random


class Critter(object):
    """Virtual cow"""
    def __init__(self, name, hunger, boredom):
        print("New pet was born!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        obj = "Objects Critter class\n"
        obj += "name: " + self.name + "\n"
        return obj

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
        return self.name

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
    animal1_name = input("How you want to call your first animal?: \n")
    hunger_1 = random.randint(1, 7)
    boredom_1 = random.randint(1, 7)
    animal_1 = Critter(animal1_name, hunger_1, boredom_1)
    animal2_name = input("How you want to call your second animal?: \n")
    hunger_2 = random.randint(1, 7)
    boredom_2 = random.randint(1, 7)
    animal_2 = Critter(animal2_name, hunger_2, boredom_2)
    animal3_name = input("How you want to call your third animal?: \n")
    hunger_3 = random.randint(1, 7)
    boredom_3 = random.randint(1, 7)
    animal_3 = Critter(animal3_name, hunger_3, boredom_3)
    animal4_name = input("How you want to call your fourth animal?: \n")
    hunger_4 = random.randint(1, 7)
    boredom_4 = random.randint(1, 7)
    animal_4 = Critter(animal4_name, hunger_4, boredom_4)

    # creating a list to follow the changes
    farm_1 = [animal_1.name, animal_1.hunger, animal_1.boredom]
    farm_2 = [animal2_name, animal_2.hunger, animal_2.boredom]
    farm_3 = [animal3_name, animal_3.hunger, animal_3.boredom]
    farm_4 = [animal4_name, animal_4.hunger, animal_4.boredom]

    # print(farm_1)
    # print(farm_2)
    # print(farm_3)
    # print(farm_4)

    choice = None
    while choice != "0":
        print("""
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
            animal_1.talk()
            animal_2.talk()
            animal_3.talk()
            animal_4.talk()

        # feed your pet
        elif choice == "2":
            animal_1.eat()
            animal_2.eat()
            animal_3.eat()
            animal_4.eat()
            farm_1[1] = animal_1.hunger
            farm_2[1] = animal_2.hunger
            farm_3[1] = animal_3.hunger
            farm_4[1] = animal_4.hunger

        # play with your pet
        elif choice == "3":
            animal_1.play()
            animal_2.play()
            animal_3.play()
            animal_4.play()
            farm_1[2] = animal_1.boredom
            farm_2[2] = animal_2.boredom
            farm_3[2] = animal_3.boredom
            farm_4[2] = animal_4.boredom

        # unknown choice
        else:
            print("\nSorry", choice, "is invalid.")

        # print(farm_1)
        # print(farm_2)
        # print(farm_3)
        # print(farm_4)


main()
input("\n\nFor finish press Enter.")
