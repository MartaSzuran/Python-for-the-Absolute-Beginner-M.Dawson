# program komunikat

# użytkowanik wprowadza komunikat, a program wyswietla go w odwrotnej kolejnosci

print("""

        ------------------
            KOMUNIKAT
        ------------------

    """)

message = input("Wprowadz komunikat: ")

lenght = len(message)
# print(lenght)

# start = długosc tekstu jest 5, a python liczy od 0 do 4, muszę ograniczyc zakres od dlugosc -1 
# koniec = program nie bierze pod uwage ograniczenie gornego w moim przypadku byloby to 0, zatem musze się cofnac do -1
# -1 oznacza odliczenie od tylu

for i in range(lenght - 1, -1, -1):
    print(message[i])

input("\nAby zakończyć naciśnij Enter.")
