# simple interface GUI
# creating root window


# importing whole content from module tkinter
from tkinter import *

# I don't need to add tkinter.Tk()
# I can create only one root window
root = Tk()

root.title("Simple GUI window")
root.geometry("225x100")

# start events loop
root.mainloop()
