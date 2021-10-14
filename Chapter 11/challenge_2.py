# trying cat sprite

from livewires import games, color
import random

games.init(screen_width=1000, screen_height=800, fps=50)


class Cat(games.Sprite):
    """Creating cat control with mouse."""
    image = games.load_image("cat.jpg")

    def __init__(self):
        super(Cat, self).__init__(image=Cat.image,
                                  x=games.mouse.x,
                                  y=740)

    def update(self):
        self.x = games.mouse.x

        if self.x < 0:
            self.x = 0
        if self.x > games.screen.width:
            self.x = games.screen.width

        self.check_collision()

    def check_collision(self):
        for stone in self.overlapping_sprites:
            self.destroy()
            self.end_game()

    def end_game(self):
        message = games.Message(value="THE END",
                                size=50,
                                color=color.red,
                                x=games.screen.width / 2,
                                y=games.screen.height / 2,
                                lifetime=2 * games.screen.fps,
                                after_death=games.screen.quit)
        games.screen.add(message)


class Stone(games.Sprite):

    def __init__(self, x, image, dy):
        super(Stone, self).__init__(image=image,
                                    x=x,
                                    y=0,
                                    dy=dy)

    def update(self):
        if self.y > games.screen.height:
            stones_generator()
            self.destroy()


def stones_generator():
    stone_choose = random.randint(1, 3)
    place_choose = random.randint(20, 980)
    stone_1 = games.load_image("stone.jpg")
    stone_2 = games.load_image("stone_2.jpg")
    stone_3 = games.load_image("stone_3.jpg")

    if stone_choose == 1:
        the_stone = Stone(x=place_choose,
                          image=stone_1,
                          dy=stone_choose)
        games.screen.add(the_stone)
    elif stone_choose == 2:
        the_stone = Stone(x=place_choose,
                          image=stone_2,
                          dy=stone_choose)
        games.screen.add(the_stone)
    else:
        the_stone = Stone(x=place_choose,
                          image=stone_3,
                          dy=stone_choose)
        games.screen.add(the_stone)


def main():
    sky_image = games.load_image("sky.jpg", transparent=False)
    games.screen.background = sky_image

    the_cat = Cat()
    games.screen.add(the_cat)

    stones_generator()
    stones_generator()
    stones_generator()

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


main()
