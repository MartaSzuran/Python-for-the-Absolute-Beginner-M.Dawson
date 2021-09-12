# Simple game
# Shows module import

import games, random

print("\t\tWelcome in the simplest game in the world!!.")

again = None
while again != "n":
    players = []
    # to use other module function: module name + '.' + function name
    num = games.ask_number(question="Give me number of players (2 - 5):", low=2, high=5)

    for i in range(num):
        name = input("Players name: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("\nScores are:")
    for player in players:
        print(player)

    again = games.ask_yes_no("\nDo you want to play again? (y/n): ")


input("\n\nFor finish press Enter.")
