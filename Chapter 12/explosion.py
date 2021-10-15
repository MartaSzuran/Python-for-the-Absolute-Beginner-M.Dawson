# explosion using animation

from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


image = games.load_image("nebulae.jpg", transparent=False)
games.screen.background = image

# constructor Animation class takes as an argument list of pictures
# creating list of pictures
explosion_file = ["explosion1.bmp",
                  "explosion2.bmp",
                  "explosion3.bmp",
                  "explosion4.bmp",
                  "explosion5.bmp",
                  "explosion6.bmp",
                  "explosion7.bmp",
                  "explosion8.bmp",
                  "explosion9.bmp"]

# creating explosion object and add it to the screen
explosion = games.Animation(images=explosion_file,
                            x=games.screen.width/2,
                            y=games.screen.height/2,
                            # if attribute n_repeats is 0 it will endless make animation
                            n_repeats=0,
                            # repeat_interval shows delay between pictures one after another
                            repeat_interval=5)
games.screen.add(explosion)

games.screen.mainloop()
