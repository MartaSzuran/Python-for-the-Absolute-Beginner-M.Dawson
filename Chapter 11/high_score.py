# High score
# shows creating a text on screen

from livewires import games, color
# color module can be used in objects Text and Message

games.init(screen_width=640, screen_height=480, fps=50)

# using function load_image from games
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

# create text object
score = games.Text(value=1756521,
                   size=60,
                   color=color.black,
                   x=550,
                   y=30)

# add object to screen
games.screen.add(score)

games.screen.mainloop()
