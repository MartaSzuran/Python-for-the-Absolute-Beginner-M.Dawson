# paddle for challenge 3

# creating paddle which moves with the mouse on the bottom of the screen

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


class Paddle(games.Sprite):
    """Creating paddle which moves with the mouse on the bottom of the screen."""
    image = games.load_image("paddle.jpg")

    def __init__(self):
        super(Paddle, self).__init__(image=Paddle.image,
                                     x=games.mouse.x,
                                     y=games.screen.height-10)

    def update(self):
        self.x = games.mouse.x

        if self.x < 0:
            self.x = 0
        if self.x > games.screen.width:
            self.x = games.screen.width


def main():
    background_image = games.load_image("sky.jpg", transparent=False)
    games.screen.background = background_image

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


main()
