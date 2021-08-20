# program Kreator postaci

# użytkkownik ma pule pkt ktore moze spozytkowac na cztery atrybuty



# przywitanie

print("""

        {{ WITAJ W GRZE KREATOR POSTACI }}
           { WYBIERZ / ZAMIEN ATRYBUT }

""")

# tworzenie slownika atrybutow
attributes = {"sila" : "0", "zdrowie": "0", "madrosc": "0", "zrecznosc": "0"}
print("Masz:", attributes)

# pula punktow do wykorzystania 30
points = 30
print("Rozdysponuj", points, "puntow na rozne atrybuty.")

print("""
0 - zakoncze
1 - dodaj punkty
2 - odejmij punkty
""")

choice = None
while choice != "0":

    choice = input("Co wybierasz? \n")
    
    if choice == "1":
        
        chosen_attribute = input("Atrybut, ktoremu chcesz przydzielic punkty to: \n")

        if chosen_attribute in attributes:
            print("Masz:", points, "punktow\n")
            points_for_addition = int(input("Ile punktow chcesz przeznaczyc: "))
            if points_for_addition > points:
                print("Nie masz wystarczajacej ilosci punktow")
            else:
                attributes[chosen_attribute] = points_for_addition
                points -= points_for_addition
                print("Puntky zostaly przydzielone!")
                print("Zostało Ci:",points, "punktow")             
        else:
            print("Nie ma takiego atrybutu, atrybuty do wyboru to: ", attributes.keys())

    elif choice == "2":
        
        chosen_attribute = input("Atrybut, ktoremu chcesz odebrac punkty to: \n")

        if chosen_attribute in attributes:
            points_on_atrribute = int(attributes[chosen_attribute])
            print("Masz", points_on_atrribute,"przydzielone na ten atyrbut.") 
            points_for_subtraction = int(input("Ile punktow chcesz odebrac? \n"))
            points_left = points_on_atrribute - points_for_subtraction
            
            if points_left < 0:
                print("Nie masz tylu punktów przydzielonych na ten atrybut.")
            else:
                attributes[chosen_attribute] = points_left
                print("Puntky zostaly odjete!")
                points += points_for_subtraction
                print("Zostało Ci:",points, "punktow")
        else:
            print("Nie ma takiego atrybutu, atrybuty do wyboru to: ", attributes.keys())
        
    else:
        print("Dziekujemy za gre!!.")
        
    print("""
    0 - zakoncze
    1 - dodaj punkty
    2 - odejmij punkty
    """)
    print("Masz:", attributes)
    
input("Aby zakończyc gre nacisnij klawisz Enter.")
