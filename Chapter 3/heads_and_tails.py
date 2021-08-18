# program liczący losową liczbę reszek i
# orzełków wypadających w 100 rzutach

import random

input("Gdy naciśniesz enter, program dokona 100 rzutów, a następnie powie Ci ile razy wypadła reszka, a ile razy orzelek")

orzelek = 0
reszka = 0
ilosc_rzutow = 0


while ilosc_rzutow < 100:
    rzut = random.randint(1,2)
    if rzut == 1:
        orzelek += 1
        # print("orzelek:", orzelek)
    else:
        reszka += 1
        # print("reszka:", reszka)
    ilosc_rzutow += 1
    # print(ilosc_rzutow)

print("\n\nW 100 rzutach wypadło", orzelek, "orzełków, a", reszka, "reszek")

input("Aby zakończyć program naciśnij enter.")
