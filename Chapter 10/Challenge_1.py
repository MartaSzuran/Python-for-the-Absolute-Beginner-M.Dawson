# Mad Lib 2
# different layout

from tkinter import *


class Application(Frame):
    """GUI Application for create story with usage of words given by user."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets."""
        # create label with instruction
        Label(self,
              text="Choose words to create your own story.",
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # create label for choosing a name
        Label(self,
              text="Choose name: ",
              ).grid(row=1, column=0, sticky=W)

        # create radio buttons for choosing a name
        self.name_entry = StringVar()
        self.name_entry.set(None)

        names = ["Elizabeth", "Virginia", "Mary"]
        column = 1
        for name in names:
            Radiobutton(self,
                        text=name,
                        variable=self.name_entry,
                        value=name,
                        ).grid(row=1, column=column, sticky=W)
            column += 1

        # create text field to input one noun
        # create Label: input a noun
        Label(self,
              text="Input one noun: "
              ).grid(row=2, column=0, sticky=W)

        # create text field
        self.noun_entry = Entry(self)
        self.noun_entry.grid(row=2, column=1, columnspan=1, sticky=W)

        # create label to choose place
        Label(self,
              text="Choose place: ",
              ).grid(row=3, column=0, sticky=W)

        # create check button to choose place castle
        self.castle = BooleanVar(self)
        Checkbutton(self,
                    text="castle",
                    variable=self.castle,
                    ).grid(row=3, column=1, sticky=W)

        # create check button to choose place mountain temple
        self.mountain_temple = BooleanVar(self)
        Checkbutton(self,
                    text="mountain temple",
                    variable=self.mountain_temple,
                    ).grid(row=3, column=2, sticky=W)

        # create check button to choose place beach cottage
        self.beach_cottage = BooleanVar(self)
        Checkbutton(self,
                    text="beach cottage",
                    variable=self.beach_cottage,
                    ).grid(row=3, column=3, sticky=W)

        # create label to choose verb
        Label(self,
              text="Choose verb:",
              ).grid(row=4, column=0, sticky=W)

        # create a text field for a verb
        self.verb_entry = Entry(self)
        self.verb_entry.grid(row=4, rowspan=2, column=1, sticky=W)

        # create submit button
        Button(self,
               text="submit",
               command=self.tell_story
               ).grid(row=5, column=0, columnspan=3, sticky=W)

        # create text field containing story
        self.tell_story_txt = Text(self, width=100, height=500, wrap=WORD)
        self.tell_story_txt.grid(row=6, column=0, columnspan=5, sticky=W)

    def tell_story(self):
        """Input into text field new story"""
        name = self.name_entry.get()
        verb = self.verb_entry.get()
        noun = self.noun_entry.get()

        places = ""
        if self.castle.get():
            places += "castle, "
        if self.mountain_temple.get():
            places += "mountain temple, "
        if self.beach_cottage.get():
            places += "beach cottage. "

        # create the story
        story = "There was a princess called "
        story += name
        story += " She lived in a "
        story += places
        story += "where she "
        story += verb
        story += " and keep "
        story += noun

        # show the story
        self.tell_story_txt.delete(0.0, END)
        self.tell_story_txt.insert(0.0, story)


# main
root = Tk()
root.title("Mad Lib 2")
app = Application(root)
app.mainloop()
