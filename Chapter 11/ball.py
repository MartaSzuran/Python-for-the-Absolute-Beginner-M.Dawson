# ball for challenge 3

from livewires import games


games.init(screen_width=1000, screen_height=800, fps=50)


class Ball(games.Sprite):
    image = games.load_image("stone.jpg")
    """Creating bouncing ball sprite."""
    def __init__(self):
        super(Ball, self).__init__(image=Ball.image,
                                   x=games.screen.width/2,
                                   y=0,
                                   dx=2,
                                   dy=2)

    def update(self):
        """Change move after touching the edges."""
        if self.x < 0 or self.x > games.screen.width:
            self.dx = -self.dx
        if self.y < 0 or self.y > games.screen.height:
            self.dy = -self.dy


def main():
    background_image = games.load_image("sky.jpg", transparent=False)
    games.screen.background = background_image

    the_ball = Ball()
    games.screen.add(the_ball)

    games.screen.mainloop()


main()
