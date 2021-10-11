# Make an order!
# user choose dish from menu with prices and then show total price

from tkinter import *


class Application(Frame):
    """Menu Gui Application."""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.total_price = 0

    def create_widgets(self):
        """Create widgets for the menu."""
        # create menu label
        Label(self,
              text="Menu"
              ).grid(row=0, column=1, sticky=W)

        # create dishes list
        dishes = ["Pizza margherita", "Pizza salame", "Pizza carbonara"]

        # create variables used for iteration
        row = 1
        column = 0

        # pizza margherita
        for dish in dishes:
            # create label for dishes
            Label(self,
                  text=dish,
                  ).grid(row=row, column=column, columnspan=2, sticky=W)

            # create label for prices
            Label(self,
                  text="Price: "
                  ).grid(row=row, column=column+2, sticky=W)
            row += 1

        # create list for prices
        self.prices = ["15", "20", "25"]
        row = 1
        for price in self.prices:
            self.price_text = Text(self, width=2, height=1, wrap=WORD)
            self.price_text.grid(row=row, column=column+3, sticky=W)
            self.price_text.insert(0.0, price)
            row += 1

        # create dishes checkbutton
        self.is_margharita = BooleanVar()
        Checkbutton(self,
                    variable=self.is_margharita,
                    ).grid(row=1, column=4, sticky=W)

        self.is_salame = BooleanVar()
        Checkbutton(self,
                    variable=self.is_salame,
                    ).grid(row=2, column=4, sticky=W)

        self.is_carbonara = BooleanVar()
        Checkbutton(self,
                    variable=self.is_carbonara,
                    ).grid(row=3, column=4, sticky=W)

        # create button for counting total price
        Button(self,
               text="Total",
               command=self.count_total,
               ).grid(row=4, column=2, sticky=W)

        # create text field to write total sum
        self.results = Text(self, width=5, height=2, wrap=WORD)
        self.results.grid(row=5, column=2, columnspan=3, sticky=W)

    def count_total(self):
        """Taking prices and count total price for dishes."""
        total = self.total_price

        if self.is_margharita.get():
            total += int(self.prices[0])
        if self.is_salame.get():
            total += int(self.prices[1])
        if self.is_carbonara.get():
            total += int(self.prices[2])

        self.results.delete(0.0, END)
        self.results.insert(0.0, total)


root = Tk()
root.title("Pizzeria menu.")
app = Application(root)
app.mainloop()
