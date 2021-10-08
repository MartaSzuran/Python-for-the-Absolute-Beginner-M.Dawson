# labeler
# showing label

from tkinter import *

root = Tk()
root.title("Labeler")
root.geometry("500x800")


# widgets = window gadgets
# labels are not interactive

# creating frame for keeping labels there
# while creating new widgets you need to pass master object (in this case root)
app = Frame(root)
# new frame is inside root window


# all widgets has method grid
# it is connected to layout manager (you can plan where widgets are in window)
app.grid()


# creating label
lbl = Label(app, text="I am label!")

# grid method makes us see label
lbl.grid()

# start events loop
root.mainloop()
