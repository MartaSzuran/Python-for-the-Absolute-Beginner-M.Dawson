# game about traveler who visits different planets

import random


class Traveler(object):
    """Game character."""
    def __init__(self, name, health=100, hunger=0, endurance=100):
        self.name = name
        self.health = health
        self.hunger = hunger
        self.endurance = endurance

    def __str__(self):
        representation = self.name + " you have " \
                         "\nhealth: " + str(self.health) + \
                         "\nhunger: " + str(self.hunger) + \
                         "\nendurance: " + str(self.endurance)
        return representation

    def travel(self, planets):
        choose = input("\nWhat planet you would like to visit \n"
                       "(PlanetGarden - 1/ PlanetMountain - 2/ PlanetHospital - 3): ")
        while choose:
            if choose == "1":
                print("Lets fly to PlanetGarden.\n")
                choose = planets[0]
                break
            elif choose == "2":
                print("Lets fly to PlanetMountain.\n")
                choose = planets[1]
                break
            elif choose == "3":
                print("Lets fly to PlanetHospital.\n")
                choose = planets[2]
                break
            else:
                print("There is not such planet in our universe, try again!")
                choose = input("\nWhat planet you would like to visit \n"
                               "(PlanetGarden - 1/ PlanetMountain - 2/ PlanetHospital - 3): \n")
        return choose


class Planet(object):
    """Planet project."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        representation = "Planet" + self.name + ".\n"
        return representation


class PlanetGarden(Planet):
    """Planet with food supplies."""
    def __init__(self, food=25):
        super(Planet, self).__init__()
        self.food = food

    def __str__(self):
        representation = "You gain " + str(self.food) + " on PlanetGarden!"
        return representation

    def special(self, points):
        points -= 25
        return points


class PlanetMountain(Planet):
    """Planet where traveler practice for better endurance."""
    def __init__(self, cardio=25):
        super(Planet, self).__init__()
        self.cardio = cardio

    def __str__(self):
        representation = "You gain " + str(self.cardio) + " on PlanetMountain"
        return representation

    def special(self, points):
        points += 25
        return points


class PlanetHospital(Planet):
    """Planet where traveler can heal himself."""
    def __init__(self, heal=25):
        super(Planet, self).__init__()
        self.heal = heal

    def __str__(self):
        representation = "You gain " + str(self.heal) + " on PlanetHospital"
        return representation

    def special(self, points):
        points += 25
        return points


class Enemies(object):
    def __init__(self, name, force=0):
        self.name = name
        self.force = force

    def __str__(self):
        representation = self.name
        return representation

    def hit(self):
        punch = random.randint(5, self.force)
        return punch

    def meet_enemy(self, points, punch):
        points -= punch
        return points


class Game(object):
    """Traveler."""
    print("\t\tWELCOME TO GAME TRAVELER.\n\t\tjust try not to die ...\n")

    def __init__(self, name):
        self.name = name

    def __str__(self):
        representation = self.name
        return representation

    def lose(self):
        print(self.name, "loses.")

    def wins(self):
        print(self.name, "wins")


def main():
    # creating new game
    name = input("What's your name? ")
    game = Game(name)

    # creating traveler
    traveler = Traveler(name)
    print(traveler)

    # game action
    response = input("\nWould you like to travel? (y/n): \n")
    while response != "n":
        if response == "y":
            planet_1 = PlanetGarden()
            planet_2 = PlanetMountain()
            planet_3 = PlanetHospital()

            enemy_1 = Enemies(name="Fat_dragon", force=30)
            enemy_2 = Enemies(name="Space_runner", force=40)
            enemy_3 = Enemies(name="Killer", force=60)

            enemies = [enemy_1, enemy_2, enemy_3, "Free passage\n"]
            planets = [planet_1, planet_2, planet_3]
            choose = traveler.travel(planets)

            enemy_who_traveler_meats = random.choice(enemies)

            if enemy_who_traveler_meats != enemies[3]:
                print("\nOn you way you meat", enemy_who_traveler_meats)

            if enemy_who_traveler_meats == enemy_1:
                punch = enemy_1.hit()
                enemy_1.meet_enemy(points=traveler.hunger, punch=punch)
                print("Enemy", enemy_1, "attacks you and after great fight you have won! "
                      "Unfortunately you have gain", punch, "points to your hunger.\n")
                traveler.hunger += punch

            elif enemy_who_traveler_meats == enemy_2:
                punch = enemy_2.hit()
                enemy_2.meet_enemy(points=traveler.endurance, punch=punch)
                print("Enemy", enemy_2, "challenged you for the race! You had enough endurance to win."
                      " Unfortunately you have lost", punch, "from your endurance.\n")
                traveler.endurance -= punch
            elif enemy_who_traveler_meats == enemy_3:
                punch = enemy_3.hit()
                enemy_3.meet_enemy(points=traveler.health, punch=punch)
                print("You have met the hardest enemy of all in whole wide space ", enemy_3,
                      ".\nUnfortunately you have lost", punch, "from your health.\n")
                traveler.health += punch
            else:
                print(enemies[3])

            if traveler.hunger >= 50:
                game.lose()
                print("You have died from hunger!!")
            elif traveler.endurance == 0:
                game.lose()
                print("You have died because emaciation!!")
            elif traveler.health == 0:
                game.lose()
                print("You have been killed!!")
            else:
                print("\tYou have survived space travel!!\n")

            if choose == planet_1:
                traveler.hunger = choose.special(traveler.hunger)
                print(planet_1)
                print(traveler)
            elif choose == planet_2:
                traveler.endurance = choose.special(traveler.endurance)
                print(planet_2)
                print(traveler)
            else:
                traveler.health = choose.special(traveler.health)
                print(planet_3)
                print(traveler)

            if traveler.hunger <= 0 and traveler.endurance >= 200 and traveler.health >= 200:
                game.wins()
                print("You are the winner!!")
                break

            response = input("\nWould you like to travel more? (y/n): \n")


main()

print("\nThank you for playing.")
input("\nPress enter to finish")
