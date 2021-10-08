# longevity (długowieczność)
# program showing usage of widgets Entry, Text and manager of layout Grid

from tkinter import *


class Application(Frame):
    """Application with GUI, which can revealed secret of longevity."""
    def __init__(self, master):
        """Initialize frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create widgets Button, Text and Entry."""
        # create label with instruction
        self.inst_lbl = Label(self, text="Input password to longevity secret.")

        # using manager Grid to locate the label (grid = siatka)
        # row, column takes as argument intagers
        # columnspan=2 - button of size: one row wide 2 columns
        # there is also rowspan
        # sticky takes as argument sides of world : N,S,W,E
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        # create label to password
        self.pw_lbl = Label(self, text="Password: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        # widget type Entry
        # entry field where user can input text
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # create accept button
        # connectiong button with reveal action (show secret after input password)
        self.subbmit_bttn = Button(self, text="Subbmit", command=self.reveal)
        self.subbmit_bttn.grid(row=2, column=0, sticky=W)

        # create widget Text
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    # method check if user input valid password
    def reveal(self):
        """Print message depends of password validation."""
        # return text from widget
        contents = self.pw_ent.get()

        if contents == "secret":
            message = "This is a secret of longevity: live till you are 99 years old, " \
                      "and then be VERY careful."
        else:
            message = "Invalid password."

        # to put message into widget Text I need to erase all previouse content using delete method
        # delete method erase text from text widgets
        # 0.0 represents 0(rows).0(columns) <- absolute beginning of text field
        # END means end of text field
        self.secret_txt.delete(0.0, END)
        # putting text I want in that text field using insert()
        self.secret_txt.insert(0.0, message)


# main
root = Tk()
root.title("Longevity")
root.geometry("300x150")

app = Application(root)

root.mainloop()
