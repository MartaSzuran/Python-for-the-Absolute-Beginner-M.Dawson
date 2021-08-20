# Szubienica


# Gra w szubienice polega na wylosowaniu slowa przez kompter
# uzytkownik musi odgadnac poszczegolne litery
# jezeli gracz nie odgadnie w pore slowa, maly ludzik zostaje powieszony
# przyklad z ksiazki

# tworzenie stalych


import random

HANGMAN = (
"""
-------
|     |
|
|
|
|
-----------
""",
"""
-------
|     |
|     0
|
|
|
-----------
""",
"""
-------
|     |
|     0
|     +
|
|
|
|
-----------
""",
"""
-------
|     |
|     0
|    /+
|
|
|
|
-----------
""",
"""
-------
|     |
|     0
|    /+/
|
|
|
|
-----------
""",
"""
-------
|     |
|     0
|    /+/
|
|
|
|
-----------
""",
"""
-------
|     |
|     0
|    /+/
|     |
|
|
|
-----------
""",
"""
-------
|     |
|     0
|    /+/
|     |
|    |
|    |
|
-----------
""",
"""
-------
|     |
|     0
|    /+/
|     |
|    | |
|    | |
|
-----------
""")

# zmienna reprezentujaca ilosc nieudanych prob jest rowna dlugosci krotki hangman - 1
# (-1 poniewaz pierwszy szubienica wyswietli sie przed zgadywaniem)
MAX_WRONG = len(HANGMAN) - 1

# lista słow
WORDS = ("LAMPA", "KALESONY", "PIJAWKA", "BERET", "ROWER")

# wybieramy slowo do odgadniecia
word = random.choice(WORDS)
print(word)

# lancuch przedsatawiajacy to co graczowi udalo sie odgadnac
# kreska zastepuje nieodgadnieta literke, ilosc kreser = ilosci liter w slowie
so_far = "-" * len(word)

# ilosc nieudanych prob
wrong = 0

# lista liter juz odgadnietych przez gracza
used_letters = []

# glowna petla programu

print("Witaj w grze szubienica. Powodzenia!")

# jezeli wrong jest mniejsze niz ilosc rysunkow szubienicy
# i literki odganieta przez uzytkownika nie sa rowne slowie nie wychodz z petli
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nWykorzystales juz nastepujace litery:\n", used_letters)
    print("\nNa razie zagadkowe slowo wyglada tak:\n", so_far)

    # pobieranie litery od gracza
    guess = input("\n\nWprowadz litere: ")
    guess = guess.upper()

    while guess in used_letters:
        print("Juz wykorzystales litere", guess)
        guess = input("Wprowadz litere: ")
        guess = guess.upper()
        
    # dodajemy litere do used_letters
    used_letters.append(guess)

    # sprawdzamy czy litera jest w slowie

    if guess in word:
        print("\nTak!", guess, "znajduje sie w zgadkowym slowie!")

        # tworzymy nowa wersje so_far
        new = ""
        for i in range(len(word)):

            # jeżeli literka jest rowna literce na danym miejscu w slowie to ja zapisuje w new
            if guess == word[i]:
                new += guess
            else:
                # jeżeli literki nie ma pod danym elementem to zapisuje - z so_far
                new += so_far[i]

        # zapisuje lancuch new pod zmienna so_far
        so_far = new
        
    else:
        print("\nNiestety", guess, "nie wystepuje w zagadkowym slowie.")
        wrong += 1

# zakonczenie gry oraz podanie wyniku

if wrong == MAX_WRONG:
    print(HANGMANA[wrong])
    print("\nZostales powieszony!")
else:
    print("\nOdgadles!")

print("\nZagadkowe slowo to", word)

input("\n\nAby zakonczyc program, nacisnij klawisz Enter.")
                
    








