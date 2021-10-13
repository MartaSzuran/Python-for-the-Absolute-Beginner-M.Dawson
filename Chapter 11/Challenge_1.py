# pizza panic
# player need to catch falling pizzas, before it touches the bottom
# Challenge 1 - increase pizzas and cook movement

from livewires import games, color
import random


games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    """Pan control by player, using to catch pizzas."""
    image = games.load_image("fry_pan.bmp")

    def __init__(self):
        """Initialize Pan object and create Text object for store score."""
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)

        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width-10)

        games.screen.add(self.score)

    def update(self):
        """Change position for one shown by mouse."""
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_catch()

    def check_catch(self):
        """Method check if user catch any pizza."""
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            # score right makes sure that the score is always 10 pixels from the edge of the screen
            # beside how many integers number of scores has
            self.score.right = games.screen.width - 10
            pizza.handle_caught()


class Pizza(games.Sprite):
    """Pizza, falling down to the bottom."""
    image = games.load_image("pizza.bmp")
    speed = 1

    def __init__(self, x, y=90):
        # every new pizza is initializing on the high 90 so in the middle of cooks chest
        """Initialize Pizza object."""
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x, y=y,
                                    dy=Pizza.speed)

        # increase pizza falling
        # I need to make constant change for any other pizza
        # every new pizza will have bigger speed
        Pizza.speed += 0.02

    def update(self):
        """Check if the bottom pizza edge touches bottom of the screen."""
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def faster_pizza(self):
        if Pan.score > 100:
            self.speed += 1

    def handle_caught(self):
        """Destroy self if caught."""
        # destroy method makes pizza vanished
        self.destroy()

    def end_game(self):
        """If pizza touches bottom of the screen end_game."""
        end_message = games.Message(value="END GAME",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """Kitchen chef, who moves right, left, and drops pizzas."""
    image = games.load_image("cook.bmp")

    def __init__(self, y=55, speed=2, odds_change=200):
        """Initialize chef object."""
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        """check, if movement direction has to be changed to opposite."""
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        """Reduce time counter or drop pizza and reset settings."""
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            # give chef coordinates to make sure that pizza will show in the same place as chef
            # increase falling speed after 50 pkt
            new_pizza = Pizza(x=self.x)
            games.screen.add(new_pizza)

            # set the margin for less then 30% of pizza height, independently from pizza speed
            # this is the distance between pizzas
            self.time_til_drop = int(new_pizza.height * 1.3 / Pizza.speed) + 1
            # increase speed of cook movement
            self.dx += 1


def main():
    """Run game."""
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_pan = Pan()
    games.screen.add(the_pan)

    games.mouse.is_visible = False

    games.screen.event_grab = True
    games.screen.mainloop()


# run game
main()
