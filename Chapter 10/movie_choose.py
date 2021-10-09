# Choose movie
# shows choice fields (square)

from tkinter import *


class Application(Frame):
    """Gui application for choosing your favorite movie genre."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets used for choosing movie genre."""
        # create label with description
        # without variable
        # this feature is available because tkinter library
        # but only when I do not need direct access to this label
        Label(self,
              text="Choose your favorite movie genre."
              ).grid(row=0, column=-0, sticky=W)

        # create label with instruction
        Label(self,
              text="Mark which you would like to choose."
              ).grid(row=1, column=0, sticky=W)

        # create choose field with booleanVar from tkinter
        # likes_comedy = attribute
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text="comedy",
                    variable=self.likes_comedy,
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        self.likes_drama = BooleanVar()
        Checkbutton(self,
                    text="drama",
                    variable=self.likes_drama,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        self.likes_horror = BooleanVar()
        Checkbutton(self,
                    text="horror",
                    variable=self.likes_horror,
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # create text field showing results
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """Actualize text field and print favorite users movies genres."""
        likes = ""
        # using get() method from object BooleanVar
        if self.likes_comedy.get():
            likes += "You like comedy movies.\n"

        if self.likes_drama.get():
            likes += "You like drama movies.\n"

        if self.likes_horror.get():
            likes += "You like horror movies.\n"

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)

# main
root = Tk()
root.title("Choose movie genre.")
app = Application(root)
root.mainloop()
