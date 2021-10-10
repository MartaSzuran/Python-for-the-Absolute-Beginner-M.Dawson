# Choose movie 2
# shows choice fields (circles)

from tkinter import *


class Application(Frame):
    """Gui application for choosing your favorite movie genre."""
    def __init__(self, master):
        """Make a frame"""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets used for choosing movie genre."""
        # create label with description
        Label(self,
              text="Choose your favorite movie genre."
              ).grid(row=0, column=-0, sticky=W)

        # create label with instruction
        Label(self,
              text="Mark which genre you would like to choose."
              ).grid(row=1, column=0, sticky=W)

        # create variable, which is a representation for single button, with favorite movie genre
        # StringVar object
        # self.favorite = attribute
        self.favorite = StringVar()
        self.favorite.set(None)

        # comedy button
        # if button comedy is chosen object StringVar is containing string comedy (self.favorite (value) ="comedy")
        Radiobutton(self,
                    text="comedy",
                    variable=self.favorite,
                    value="comedy",
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        Radiobutton(self,
                    text="romance",
                    variable=self.favorite,
                    value="romance",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        Radiobutton(self,
                    text="drama",
                    variable=self.favorite,
                    value="drama",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # creating text field to print results
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """Update text field, to print favorite movie genre."""
        message = "Your favorite movie genre is: "
        message += self.favorite.get()

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)


root = Tk()
root.title("Movie choose.")
app = Application(root)
root.mainloop()
