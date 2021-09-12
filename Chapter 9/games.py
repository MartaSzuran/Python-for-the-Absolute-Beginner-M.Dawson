# Games
# shows creating a module

class Player(object):
    """Game player."""
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":t" + str(self.score)
        return rep


def ask_yes_no(question):
    """Ask question, which answers are yes or no."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number from particular range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("You have start this module directly (instead of importing it).")
    input("\n\nFor finish press Enter.")
