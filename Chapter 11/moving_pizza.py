# moving pizza
# shows using parameters of sprite movement speed

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

# using function load_image from games
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

pizza_image = games.load_image("pizza.bmp")

the_pizza = games.Sprite(image=pizza_image,
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
