# moving fry pan
# shows how to use input from mouse

from livewires import games

# init function creates mouse sprite too
games.init(screen_width=640, screen_height=480, fps=50)


# create class pan
class Pan(games.Sprite):
    """Object Pan control with mouse."""
    def update(self):
        """Give mouse x and y (coordinates)."""
        self.x = games.mouse.x
        self.y = games.mouse.y


def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    pan_image = games.load_image("fry_pan.bmp")
    the_pan = Pan(image=pan_image,
                  x=games.mouse.x,
                  y=games.mouse.y)
    games.screen.add(the_pan)

    # make mouse invisible
    games.mouse.is_visible = False

    # take signals from user
    # mouse will not leave screen when parameter = True
    # else mouse can disappear from screen
    # if you take every signal and point it to the screen you cant use mouse to close that window (use esc)
    games.screen.even_grab = True

    games.screen.mainloop()


# run game
main()
