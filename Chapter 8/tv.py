# Program simulating TV
# User can change the channel and turn up or turn down the volume

class Television(object):
    """Virtual television"""

    def __init__(self, volume, channel):
        print("This is your new television.")
        self.volume = volume
        self.channel = channel

    def change_channel(self):
        channel_number = None
        while channel_number != "0":
            channel_number = int(input("\nChoose the channel: "))
            if 0 < channel_number <= 1000:
                print("You are on channel: ", channel_number)
                self.channel = channel_number
                break
            else:
                print("Invalid channel, choose again.")
                channel_number = input("\nChoose the channel: ")

    def change_volume(self):
        print("Actual volume is: ", self.volume)
        volume_amount = self.volume
        turn_up = 1
        turn_down = 1
        changing_volume = None
        while changing_volume != "0":
            changing_volume = input("\nChange the volume choosing: + / - / mute")
            if changing_volume == "+":
                volume_amount += turn_up
                print("The volume is: ", volume_amount)
                break
            elif changing_volume == "-":
                volume_amount -= turn_down
                print("The volume is: ", volume_amount)
                break
            elif changing_volume == "mute":
                volume_amount = 0
                print("The volume is: ", volume_amount)
                break
            else:
                print("Invalid operator, choose again.")
                changing_volume = input("Change the volume choosing: + / - / mute")

        self.volume = volume_amount
        if self.volume == 0:
            self.volume = 0
        elif self.volume > 50:
            self.volume = 50


def main():
    tv = Television(volume=25, channel=1)

    choice = None
    while choice != "0":
        print("""
        Television menu:       
        0 - turn off
        1 - change the channel
        2 - change the volume        
        """)

        choice = input("You choose: ")

        if choice == "0":
            print("Goodbye")

        elif choice == "1":
            tv.change_channel()

        elif choice == "2":
            tv.change_volume()

        else:
            print("Invalid choice,", choice, "try again.")


main()
input("\n\nFor finish press Enter.")
