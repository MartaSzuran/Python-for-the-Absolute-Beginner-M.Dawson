# Gra jaka to liczba

# człowiek losuje liczbę z przedziału 1-100
# komputer musi ją odgadnąć

import random

# def added for challenge 2
def ask_number(question, guess):
    print(question)

print("\t\tGra jaka to liczba!!")
print("\tSpróbuj jak szybko poradzi sobie komputer!!")

number = int(input("Wybierz liczbę z przedziału od 1 do 100: "))
# print(number)

lower_number = 1
bigger_number = 100
guess = random.randint(lower_number, bigger_number)
comp_tries = 0
# print(guess)

while number != guess:
    if guess > number:
        print("Za duża...")
        # aktualizacja warunków granicznych w wypadku zbyt dużego numeru np. 50 powinien analizować od 1 do 49
        bigger_number = guess - 1
        guess = random.randint(lower_number, bigger_number)
        # print("dolne ograniczenie:", lower_number, "górne ograniczenie:", bigger_number)
        ask_number("Is it the number:", guess)

    else:
        print("Za mała...")
        # aktualizacja warunków granicznych w wypadku zbyt dużego numeru np. 2 powinien analizować od 3 do 100
        lower_number = guess + 1 
        # print("dolne ograniczenie:", lower_number, "górne ograniczenie:", bigger_number)
        guess = random.randint(lower_number, bigger_number)
        ask_number("Is it the number:", guess)

    comp_tries += 1


print("Komputer potrzebował", comp_tries, "prób")

input("Naciśnij enter")

    

        
