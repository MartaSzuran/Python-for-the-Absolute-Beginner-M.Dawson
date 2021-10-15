# Read keyboard key


from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


class Ship(games.Sprite):
    """Moving space ship."""
    def update(self):
        """Control ship movement with keyboard keys WSAD."""
        # function is_pressed from games module return True if key was pressed otherwise False
        # to access keys:
        # games.K + _a / _1 / _SPACE
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1


def main():
    image = games.load_image("nebulae.jpg", transparent=False)
    games.screen.background = image

    ship_image = games.load_image("ship.bmp")
    the_ship = Ship(image=ship_image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)

    games.screen.mainloop()


main()
