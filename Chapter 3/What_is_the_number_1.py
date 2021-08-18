# Jaka to liczba

# Gra polegająca na losowaniu liczby od 1 do 100
# użytkownik stara się zgadnąć
# liczy się ilość prób zanim zgadnie

import random

# powitanie użytkownika
print("\tWitaj w grze 'Jaka to liczba?'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.")

# wybór liczby oraz zapisanie jej pod wartością number   
number = random.randint(1,100)

 # zapytanie użytkownika o podanie liczby
guess = int(input("Ta liczba to? "))

# ustawienie prób na 1
tries = 1

# pętla się powtarza do momentu aż guess będzie się równać numer
while guess != number:
    if guess > number:
        print("Za duża ...")
    else:
        print("Za mała ...")

    guess = int(input("Ta liczba to? "))
    tries += 1

# gdy program wychodzi z pętli oznacza to, że warunek się spełnił i użytkownik odgadł liczbę

print("Odgadłeś, ta liczba to: ", number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób")

input("\n\nAby zakończyć grę naciśnij enter.")
