# Alien conqueror
# Shows objects cooperation
# Unified Modeling Language

class Player(object):
    """Player in shooting game."""
    def blast(self, enemy):
        print("Player hurts enemy.\n")
        enemy.die()


class Alien(object):
    """Alien in shooting game."""
    def die(self):
        print("Alien is dying in suffering for long time... 'Goodbye universe'")


# main
print("\t\tAlien death\n")

hero = Player()
invader = Alien()
hero.blast(invader)

input("\nFor finish press Enter.")

