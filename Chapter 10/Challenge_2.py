# What is the number
# using GUI interface

from tkinter import *
import random


class Application(Frame):
    """GUI application for trying to guess number which computer has chosen."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 100)
        self.tries = 0

    def create_widgets(self):
        """Create widgets."""
        # label with title
        Label(self,
              text="What's the number ??",
              ).grid(row=0, column=0, sticky=N)

        # create label for choosing number
        Label(self,
              text="Choose the number: "
              ).grid(row=1, column=0, sticky=W)

        self.number_entry = Entry(self)
        self.number_entry.grid(row=1, column=1, sticky=W)

        # create submit button
        Button(self,
               text="Try this one!",
               command=self.checking_number
               ).grid(row=1, column=2, columnspan=3, sticky=N)

        # create text field with information how many tries user take and what numbers user tries
        Label(self,
              text="Number of tries: "
              ).grid(row=2, column=0, sticky=W)
        self.tries_txt = Text(self, width=2, height=1, wrap=WORD)
        self.tries_txt.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Numbers you have already chosen: "
              ).grid(row=3, column=0, sticky=E)
        self.numbers_txt = Text(self, width=100, height=1, wrap=WORD)
        self.numbers_txt.grid(row=3, column=1, sticky=W)
        # create list for numbers chosen by user
        self.numbers = []

        # create text field with results
        self.results_txt = Text(self, width=130, height=10, wrap=WORD)
        self.results_txt.grid(row=4, column=0, columnspan=4, sticky=W)

    def checking_number(self):
        number_chosen_by_computer = self.number
        number_chosen_by_human = int(self.number_entry.get())

        if number_chosen_by_human == number_chosen_by_computer:
            result = "You are right the number is: "
            result += str(number_chosen_by_computer)
            result += ". Well done !!\n"
        elif number_chosen_by_human < number_chosen_by_computer:
            self.tries += 1
            # concatenating strings print without parenthesis
            result = "Too small ...\n"
            result += "Try again ...\n"
            self.numbers.append(number_chosen_by_human)
            # using delete function to clear the entry spot
            # from position 0 to the "end"
            self.number_entry.delete(0, "end")
        else:
            self.tries += 1
            result = "Too big ...\n"
            result += "Try again ...\n"
            self.numbers.append(number_chosen_by_human)
            self.number_entry.delete(0, "end")

        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, result)

        self.numbers_txt.delete(0.0, END)
        self.numbers_txt.insert(0.0, self.numbers)

        self.tries_txt.delete(0.0, END)
        self.tries_txt.insert(0.0, self.tries)


# main
root = Tk()
root.title("What is the number ? \n")
app = Application(root)
app.mainloop()


