# program wymieszane litery

# z krotki kilku słów losowo jest losowane jedno, a następnie miesza się jego litery
# użytkownik zgaduje
# może poprosić o podpowiedz
# jeżeli rozwiąze z podpowiedzią ma mniejsza ilość punktów niz jak bez jej użycia

import random

# sekwencja słow do wyboru dużymi literami ponieważ ma być niezmienna
WORDS = ("python", "babeczka", "ciastko", "bez", "gang")

# wybor losowego slowa z krotki
word = random.choice(WORDS)
    
# tworzenie zmiennej w celu sprawdzenie poprawnosci zgadywania oraz ograniczenia warunku
correct = word

# tworze pusty lancuch w ktorej zapisze wymieszane litery
jumble = ""

# petla sie wykonuje az word nie bedzie puste
while word:

    # generowanie losowej pozycji
    position = random.randrange(len(word))

    # dodaje wylosowana litere do mojego wczesniej utworzonego pustego lancucha
    jumble += word[position]
    # print(jumble)

    # tworzenie nowego lancucha word bez tej jednej litery
    # wycinam do tej pozycji i po tej pozycji (aby wybierac z coraz mniejszej ilosci liter w slowie)
    word = word[:position] + word[(position + 1):]
    # print(word)

# przywitanie gracza
print("""

            --------------------------
                WYMIESZANE LITERY
            --------------------------
    (Za każde słowo dobędziesz punkty równe podwojonej ilości liter)
       (Za wykorzystanie podpowiedzi zostanie odjęty jeden punkt)
           (Aby zakończyć zgadywanie naciśnij klawisz Enter)
    """)

print("\nZgadnij jakie to słowo: ", jumble)

# pobieranie odpowiedzi

guess = input("Twoje odpowiedz: ")
hints = 0
hints_used = 0
score = len(correct) * 2

# pytam do momentu aż nie będzie wlasciwej odp lub gracz nie nacisnie enter
while guess != correct and guess != "":
    print("Niestety to nie to slowo.")

    hint = input("Chcesz podpowiedz? Naciśnij jakikolwiek klawisz lub wciśnij Enter\t")
    if hint and hints < len(correct):
        print("Litera", hints + 1, "w słowie to:", correct[hints])
        hints += 1
        hints_used += 1

    if hints == len(correct):
        hints = 0
    
    guess = input("Twoja odpowiedz: ")

if guess == correct:
    print("Zgadza się!! Zgadłeś. Twój wynik to:\t", score - hints_used)

print("Dziekuje za udział w grze.")

input("\n\nAby zakończyc program, nacisnij klawisz Enter.")

