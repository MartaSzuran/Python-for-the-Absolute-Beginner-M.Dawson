# astrocrash 06
# create blowing effect for asteroids / adding class based on games.Animation

from livewires import games
import math, random

games.init(screen_width=640, screen_height=480, fps=50)


# adding classes in order (first bases then final classes)
class Wrapper(games.Sprite):
    """Sprite, which "wrap" around the screen. """
    def update(self):
        """"""
        if self.top > games.screen.height:
            self.bottom = 0

        if self.bottom < 0:
            self.top = games.screen.height

        if self.left > games.screen.width:
            self.right = 0

        if self.right < 0:
            self.left = games.screen.width

    def die(self):
        """Destroy yourself."""
        self.destroy()


class Collider(Wrapper):
    def update(self):
        """Check sprites collisions."""
        super(Collider, self).update()

        if self.overlapping_sprites:
            for sprite in self.overlapping_sprites:
                sprite.die()
            self.die()

    def die(self):
        """Destroy yourself and leave explosion."""
        new_explosion = Explosion(x=self.x, y=self.y)
        games.screen.add(new_explosion)
        self.destroy()


class Asteroid(Wrapper):
    """Asteroid flying through screen."""
    # creating constants for class Asteroid
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    images = {SMALL: games.load_image("asteroid_small.bmp"),
              MEDIUM: games.load_image("asteroid_middle.bmp"),
              LARGE: games.load_image("asteroid_big.bmp")}
    SPEED = 2
    # spawn is a number of asteroids which are created after asteroid collision
    SPAWN = 2

    def __init__(self, x, y, size):
        super(Asteroid, self).__init__(
            image=Asteroid.images[size],
            x=x, y=y,
            dx=random.choice([1, -1]) * Asteroid.SPEED * random.random()/size,
            dy=random.choice([1, -1]) * Asteroid.SPEED * random.random() / size)

        self.size = size

    def die(self):
        """Destroy asteroid."""
        # if it is not small asteroid replace it with two small once
        if self.size != Asteroid.SMALL:
            for i in range(Asteroid.SPAWN):
                new_asteroid = Asteroid(x=self.x,
                                        y=self.y,
                                        size=self.size - 1)
                games.screen.add(new_asteroid)
        super(Asteroid, self).die()


class Ship(Collider):
    """Players space ship."""
    image = games.load_image("ship.bmp")
    ROTATION_STEP = 3
    VELOCITY_STEP = .03
    sound = games.load_sound("acceleration.wav")
    # adding missile delay
    MISSILE_DELAY = 25

    def __init__(self, x, y):
        super(Ship, self).__init__(image=Ship.image, x=x, y=y)
        self.missile_wait = 0

    def update(self):
        super(Ship, self).update()

        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += Ship.ROTATION_STEP
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= Ship.ROTATION_STEP

        # use velocity when up arrow is pressed
        if games.keyboard.is_pressed(games.K_UP):
            Ship.sound.play()

            # change speed attributes depends of angle of the ship
            # counting ship angle
            angle = self.angle * math.pi/180  # change to radians

            self.dx += Ship.VELOCITY_STEP * math.sin(angle)
            self.dy += Ship.VELOCITY_STEP * -math.cos(angle)

        # shoot the missile, if space is pressed
        if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait == 0:
            new_missile = Missile(self.x, self.y, self.angle)
            games.screen.add(new_missile)
            self.missile_wait = Ship.MISSILE_DELAY

        # waiting till ship can shoot another missile
        if self.missile_wait > 0:
            self.missile_wait -= 1


class Missile(Collider):
    """Missile shoot from the ship by player."""
    image = games.load_image("missile.bmp")
    sound = games.load_sound("missile.wav")
    # distance from created missile and the ship
    BUFFER = 40
    # influence speed of missile
    VELOCITY_FACTOR = 7
    # lifetime of missile after shooting it
    LIFETIME = 40

    def __init__(self, ship_x, ship_y, ship_angle):
        """Initialisation missile sprite"""
        Missile.sound.play()

        # change to radians
        angle = ship_angle * math.pi / 180

        # count staring position
        buffer_x = Missile.BUFFER * math.sin(angle)
        buffer_y = Missile.BUFFER * -math.cos(angle)
        x = ship_x + buffer_x
        y = ship_y + buffer_y

        # count speed compounds
        dx = Missile.VELOCITY_FACTOR * math.sin(angle)
        dy = Missile.VELOCITY_FACTOR * -math.cos(angle)

        # create missile
        super(Missile, self).__init__(image=Missile.image,
                                      x=x, y=y,
                                      dx=dx, dy=dy)

        self.lifetime = Missile.LIFETIME

    def update(self):
        """Missile move controls."""
        # if lifetime is over destroy the missile
        self.lifetime -= 1
        if self.lifetime == 0:
            self.destroy()

        super(Missile, self).update()


class Explosion(games.Animation):
    """Explosion animation."""
    sound = games.load_sound("explosion.wav")
    images = ["explosion1.bmp",
              "explosion2.bmp",
              "explosion3.bmp",
              "explosion4.bmp",
              "explosion5.bmp",
              "explosion6.bmp",
              "explosion7.bmp",
              "explosion8.bmp",
              "explosion9.bmp"]

    def __init__(self, x, y):
        super(Explosion, self).__init__(images=Explosion.images,
                                        x=x, y=y,
                                        repeat_interval=4, n_repeats=1,
                                        is_collideable=False)
        Explosion.sound.play()


def main():
    # create background
    image = games.load_image("nebulae.jpg", transparent=False)
    games.screen.background = image

    # create 8 asteroids
    for i in range(8):
        x = random.randrange(games.screen.width)
        y = random.randrange(games.screen.height)
        size = random.choice([Asteroid.SMALL, Asteroid.MEDIUM, Asteroid.LARGE])
        new_asteroid = Asteroid(x=x, y=y, size=size)
        games.screen.add(new_asteroid)

    # create ship
    the_ship = Ship(x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)

    games.screen.mainloop()


main()
