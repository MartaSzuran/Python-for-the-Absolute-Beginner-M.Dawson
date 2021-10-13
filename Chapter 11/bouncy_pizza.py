# bouncy pizza (bouncy - sprężysty
# managing the edges of screen and moving sprite

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


# I need to create new sprite class for pizza
# because I want something what is not define in fundamental class Sprite
# every Sprite object has method update()
class Pizza(games.Sprite):
    """Bouncing pizza."""
    # I need to shadow method update()
    def update(self):
        """After reaching screen edge, change speed value to opposite."""
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    pizza_image = games.load_image("pizza.bmp")

    the_pizza = Pizza(image=pizza_image,
                      x=games.screen.width / 2,
                      y=games.screen.height / 2,
                      # d = delta (change)
                      # dx - positive integer moves to the right
                      # dx - negative integer moves to the left
                      # dy - positive integer moves sprite down
                      # dy - negative integer moves sprite up
                      dx=1,
                      dy=1)

    games.screen.add(the_pizza)

    games.screen.mainloop()


# run game
main()
