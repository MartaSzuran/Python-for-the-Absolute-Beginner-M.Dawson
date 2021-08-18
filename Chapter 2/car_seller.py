# Program pomocny przy sprzedaży samochodu

# użytkownik wprowadza cenę samochodu
cena_samochodu = int(input("Podaj cenę samochodu: "))

# Podatek 7%
podatek = (cena_samochodu*7)/100
# print(podatek)

# Opłata rejestracyjna 5%
opłata_rejestracyjna = (cena_samochodu*5)/100
# print(opłata_rejestracyjna)

# Prowizja przygotowawcza dealera
prowizja_dealera = 1200
# print(prowizja_dealera)

# Opłata za dostarczenie
opłata_dostawa = 250
# print(opłata_dostawa)

całkowita_cena_samochodu = cena_samochodu + podatek + opłata_rejestracyjna + prowizja_dealera + opłata_dostawa

# wynik dla użytkownika
print("Za samochód musisz zapłacić cenę: ", całkowita_cena_samochodu)

input("Aby zakończyć naciśnij Enter.")
