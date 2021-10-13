# You have won
# shows object message (short notification)

from livewires import games, color

# color module can be used in objects Text and Message

games.init(screen_width=640, screen_height=480, fps=50)

# using function load_image from games
wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

# create text object
won_message = games.Message(value="You have won!",
                            size=100,
                            color=color.red,
                            x=games.screen.width/2,
                            y=games.screen.height/2,
                            # object exist for about 5 sec
                            lifetime=250,
                            # normally games.screen.quit() finishes with: "()",
                            # but here I pass only name of that function
                            after_death=games.screen.quit)


# add object to screen
games.screen.add(won_message)

games.screen.mainloop()
