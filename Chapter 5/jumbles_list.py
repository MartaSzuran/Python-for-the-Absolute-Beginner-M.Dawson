# program wypisujacy liste slow w przypadkowej kolejnosci bez ich powtarzania

# import modulow
import random

# tworzenie listy slow
WORDS = ["babcia", "dziadek", "wnuczek", "mama", "tata"]

# tworze nowa pusta liste 
new = []

# tworze zmienna na wylosowane slowo
words_added = 0

# petla dzialajaca do konca listy WORDS
while words_added < len(WORDS):
    
    word = random.choice(WORDS)
    if word not in new:
        new.append(word)
        words_added += 1
    
print(new)

input("Nacisnij Enter")

