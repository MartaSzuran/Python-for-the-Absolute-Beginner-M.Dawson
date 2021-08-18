# ciasteczko z wróżbą

# każde uruchomienie wylosuje dla Ciebie wyjątkową wróżbę
import random

input("\tNaciśnij enter aby wylosować Twoje dzisiejsze ciasteczko z wróżbą\n")

cookie_1 = "Będziesz zdrowy!!"
cookie_2 = "Jak zapomnisz o urodzinach przyjaciela, to go stracisz!"
cookie_3 = "Uważaj jak chodzisz, możesz złamać nogę!"
cookie_4 = "Będziesz bogaty!"
cookie_5 = "Spotkasz jutro miłość Twojego życia, nie pozwól aby przeszła bokiem!"

losowa_wrozba = random.randint(1,5)

if losowa_wrozba == 1:
    print(cookie_1)
elif losowa_wrozba == 2:
    print(cookie_2)
elif losowa_wrozba == 3:
    print(cookie_3)
elif losowa_wrozba == 4:
    print(cookie_4)
else:
    print(cookie_5)

print("\t\tTeraz tylko chrup chrup")

input("\nNaciśnij enter aby zakończyć wróżenie")
