# Screen background
# Show how to set background in screen window

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

# using function load_image from games
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

games.screen.mainloop()

