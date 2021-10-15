# sound and music

from livewires import games


games.init(screen_width=640, screen_height=480, fps=50)

# load WAV file
# load_sound load only WAV files
missile_sound = games.load_sound("missile.wav")

games.music.load("music_theme.mid")

choice = None
while choice != "0":
    print("""
    Sound and music
    
    0 - finish
    1 - play missile sound
    2 - play missile sound periodically
    3 - stop playing missile sound
    4 - play music theme
    5 - play music theme periodically
    6 - stop playing music theme
    """)

    choice = input("I choose: ")
    print()

    # exit
    if choice == "0":
        print("Bye bye!")

    # handling with sound
    # play missile sound
    elif choice == "1":
        # there are 8 sound channels, I can use 8 times play, but next one will do nothing
        missile_sound.play()
        print("Playing missile sound.")

    # play missile sound periodically
    elif choice == "2":
        loop = int(input("How many times you would like to play the sound? (-1 = forever): "))
        missile_sound.play(loop)
        print("Play missile sound periodically.")

    # stop playing missile sound
    elif choice == "3":
        #  stop() function stops playing particular sound on every channel
        missile_sound.stop()
        print("Stop playing missile sound.")

    # handling with music
    # there is only one channel for music
    # accepts many different music files like WAV, MP3, OGG, MIDI

    # play music theme
    elif choice == "4":
        # music is playing from previously loaded music_theme.mid
        # music is playing once
        games.music.play()
        print("Play music theme.")

    # play music theme periodically
    elif choice == "5":
        loop = int(input("How many times you would like to play the sound? (-1 = forever): "))
        games.music.play(loop)
        print("Play music theme periodically.")

    # stop playing music theme
    elif choice == "6":
        games.music.stop()
        print("Stop playing music theme.")

    # unexpected choice
    else:
        print("\nUnfortunately,", choice, "is not correct choice.")

input("\n\nPress enter to finish.")
