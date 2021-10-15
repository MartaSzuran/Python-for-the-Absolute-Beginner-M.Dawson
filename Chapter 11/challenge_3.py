# Challenge 3

# user control the paddle which bounce the ball, if ball touches the bottom of the screen game over

from livewires import games, color


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
        if self.y < 0:
            self.dy = -self.dy

        self.check_drop()

    def handle_collision(self):
        # if there is a collision bounce faster
        self.dy = -self.dy

    def check_drop(self):
        if self.y > games.screen.height:
            self.end_game()
            self.destroy()

    def end_game(self):
        message = games.Message(value="END GAME",
                                size=25,
                                color=color.red,
                                x=games.screen.width / 2,
                                y=games.screen.height / 2,
                                lifetime=2 * games.screen.fps,
                                after_death=games.screen.quit)
        games.screen.add(message)


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

        self.check_collisions()

    def check_collisions(self):
        for ball in self.overlapping_sprites:
            ball.handle_collision()


def main():
    background_image = games.load_image("sky.jpg", transparent=False)
    games.screen.background = background_image

    the_ball = Ball()
    games.screen.add(the_ball)

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()


main()
