# Jaka to liczba

# Gra polegająca na losowaniu liczby od 1 do 100
# użytkownik stara się zgadnąć
# liczy się ilość prób zanim zgadnie

import random

# powitanie użytkownika
print("\tWitaj w grze 'Jaka to liczba?'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w 10 próbach.")

# wybór liczby oraz zapisanie jej pod wartością number   
number = random.randint(1,100)

 # zapytanie użytkownika o podanie liczby
guess = int(input("Ta liczba to? "))

# ustawienie prób na 1
tries = 1

# pętla się powtarza do momentu aż guess będzie się równać number i będzie mniej prób niż 10
while guess != number and tries < 10:
    if guess > number:
        print("Za duża ...")
    else:
        print("Za mała ...")
    guess = int(input("Ta liczba to? "))
    tries += 1
    print("Tries:", tries)

    
# gdy użytkownik odgadł liczbę wyświetla się wynik i gratulacje
if guess == number:
    print("Odgadłeś, ta liczba to: ", number)
    print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób")
else:
    print("Nie udało Ci się odgadnąć w 10 próbach, spróbuj ponownie!")

input("\n\nAby zakończyć grę naciśnij enter.")
