# program kto jest twoim ojcem

# dodanie imienia i nazwiska osoby z przyporzadkowaniem imienia i nazwiska ojca

# słownik fathers przedstawia wartość imienia i nazwiska ojca w stosunku do klucza syna
fathers = {"MIS PUCHATEK" : {"OJCIEC": "MIS GRIZZLY", "DZIADEK": "NIEDZWIEDZ POLARNY"},
           "RYCERZ BEZ PIATEJ KLEPKI" :  {"OJCIEC": "RYCERZ BEZ CZWARTEJ KLEPKI", "DZIADEK": "RYCERZ BEZ TRZECIEJ KLEPKI"},
           "BRAD PITT" : {"OJCIEC": "BOG", "DZIADEK": "KOSMICI"}}

#przywitanie
choice = None

while choice != "0":

    print("""
    Wybierz jedna z opcji:
    0 - zakończ
    1 - dodaj 
    2 - wymień
    3 - poznaj dziadka
    4 - usuń
    """)

    choice = input("Ktora opcje wybierasz: ? \n")

    if choice == "1":
        new_son = input("Podaj imie i nazwisko syna: \n")
        new_son = new_son.upper()
        if new_son not in fathers:
            new_father = input("Podaj imie i nazwisko ojca: \n")
            new_father = new_father.upper()
            fathers[new_son] = new_father
            print("Para ojciec i styn zostala dodana.")
            # print(fathers)
        else:
            print("These son and father are already in dictionary.")

    elif choice == "2":
        son_for_change = input("Ktorego syna zmienic? \n")
        son_for_change = son_for_change.upper()
        if son_for_change in fathers:
            new_son = input("Podaj imie i nazwisko syna: \n")
            new_son = new_son.upper()
            new_father = input("Podaj imie i nazwisko ojca: \n")
            del fathers[son_for_change]
            new_father = new_father.upper()
            fathers[new_son] = new_father       
            print("Zmiany zostały zachowane.")
            # print(fathers)
        else:
            print("Para syn, ojciec nie istnieje w bazie.")
            
    elif choice == "3":
        son = input("Podaj imie lub nazwisko syna, aby poznać jego dziadka: \n")
        son = son.upper()
        if son in fathers:
            grandfather = fathers[son]["DZIADEK"]
            print("Dziadek", son, "to: ", grandfather)
        else:
            print("Syn nieobecny w bazie.")
            
    elif choice == "4":
        son_for_delete = input("Podaj imie i nazwisko syna w celu usuniecia pozycji: \n")
        son_for_delete = son_for_delete.upper()
        if son_for_delete in fathers:
            del fathers[son_for_delete]
            print("Para ojciec i syn zostali usunieci.")
            # print(fathers)
        else:
            print("Para syn, ojciec nie istnieje w bazie.")
    
    elif choice == "0":
        print("Do widzenia.")
        
    else:
        print("Niestety nieprawidlowy wybor.")

input("Aby zakończyć program wcisnij klawisz Enter.")
            
