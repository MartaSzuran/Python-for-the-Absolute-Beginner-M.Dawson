# Lazy buttons
# creating buttons

from tkinter import *

# creating main window
root = Tk()
root.title("Lazy bottoms")
root.geometry("300x500")

# creating frame for widgets
app = Frame(root)
app.grid()

# creating button in frame
bttn1 = Button(app, text="I do nothing!")
bttn1.grid()

# creating second button in different way
bttn2 = Button(app)
bttn2.grid()

# I can configure button after creating is using configure method
bttn2.configure(text="Me too!")

# creating third button using dictionary type access
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "The same thing works with me!"

# creating main loop
root.mainloop()