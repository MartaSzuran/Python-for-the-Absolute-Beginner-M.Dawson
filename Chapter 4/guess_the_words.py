# Gra zgadnij slowo

# komputer wybiera słowo
# użytkownik ma możliwość zadanie 5 pytan czy litera jest w slowie
# po wykorzystaniu pytan uzytkownik podaje propozycje rozwiazania

import random

# tworze niemutowalna liste slow
WORDS = ("korek", "babka", "laleczka", "kwiat")

word = random.choice(WORDS)

print("""

        ---------------------
            ZGADNIJ SŁOWO
        ---------------------
    (KOMPUTER PODAJE CI DLUGOSC SLOWA)
(MASZ 5 PYTAN O LITERY CZY SA ZAWARTE W TYM SLOWIE)
    (PODAJESZ ROZWIAZANIE - POWODZENIA)
    """)

print("Długość słowa to:", len(word), "liter.")

asks = 0
while asks < 5:
    letter = input("Czy w słowie jest litera: ")
    if letter in word:
        print("Tak!")
    else:
        print("Nie...")
    asks += 1

answer = input("To słowo to:")

if answer == word:
    print("Gratulacje zgadłeś")
else:
    print("Niestety nie udało Ci się.")

print("Dziękujemy za gre.")
print("Aby zakończyć wciśnij Enter.")
    
