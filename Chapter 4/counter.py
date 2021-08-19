# Program umożliwiający odliczanie

# Użytkownik może prowadzić liczbę początkową, końcową oraz odstęp

print("""
            ------------------
                WYLICZANKA
            ------------------
    """)

# wyliczanie uwzględni liczbę startowa
start = int(input("Wprowadz liczbe poczatkowa: "))

# wyliczanie nie uwzględni liczby koncowej, zatem jeżeli jest mi potrzebna powinnam
# ograniczyć do tej liczby + 1
end = int(input("Wprowadz liczbe koncowa: "))

# co jaka wartosc bedzie odliczac
step = int(input("Wprowadz odstep: "))

for i in range (start, end, step):
    print(i)

input("Aby zakończyć naciśnij enter")
