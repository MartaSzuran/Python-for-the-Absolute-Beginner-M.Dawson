# trying cat sprite

from livewires import games, color


games.init(screen_width=1000, screen_height=800, fps=50)


class Cat(games.Sprite):
    """Creating cat control with mouse."""
    image = games.load_image("cat.jpg")

    def __init__(self):
        super(Cat, self).__init__(image=Cat.image,
                                  x=games.mouse.x,
                                  y=740)

        self.score = games.Text(value=0, size=30, color=color.blue,
                                top=5, right=games.screen.width-20)

        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x

        if self.x < 0:
            self.x = 0
        if self.x > games.screen.width:
            self.x = games.screen.width

        self.counting_score()

    def counting_score(self):
        if self.x == 0:
            self.score.value += 10


def main():
    sky_image = games.load_image("sky.jpg", transparent=False)
    games.screen.background = sky_image

    the_cat = Cat()

    games.screen.add(the_cat)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


main()
