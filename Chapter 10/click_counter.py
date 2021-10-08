# click counter
# shows connection between events and event handler (procedura obslugi zdarzen)

from tkinter import *


class Application(Frame):
    """Application with GUI counting number of clicks."""
    def __init__(self, master):
        """Initialize frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()

    def create_widgets(self):
        """Create button which count number of clicks."""
        self.bttn = Button(self)
        self.bttn["text"] = "Number of clicks: 0"
        # connection event (click on button) with event handler (method update_count())
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """Increase counter of clicks and show its new content."""
        self.bttn_clicks += 1
        self.bttn["text"] = "Number of clicks: " + str(self.bttn_clicks)


# main
root = Tk()
root.title("Click counter")
root.geometry("200x300")

app = Application(root)

root.mainloop()