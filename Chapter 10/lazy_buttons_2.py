# Lazy buttons 2
# demonstrate using class in program which is using tkinter

from tkinter import *

# creating new class application on class frame
# it works because class object application is specialise type of object frame


class Application(Frame):
    """Application based on GUI with three buttons."""
    def __init__(self, master):
        """Initialize frame."""
        # passing master object to class application
        super(Application, self).__init__(master)
        # creating methods
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create three buttons which do nothing."""
        # all buttons are attributes object class Application
        # passing self to pass master object (Application)
        # first button
        self.bttn1 = Button(self, text="I do nothing!")
        self.bttn1.grid()

        # second button
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text="Me too!")

        # third button
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "The same thing works with me!"


root = Tk()
root.title("Lazy buttons 2")
root.geometry("400x500")

# creating app object and passing into master window
# app object call creating widgets method and make 3 buttons
# when I use app.creating_widgets() is makes buttons double
app = Application(root)

root.mainloop()
