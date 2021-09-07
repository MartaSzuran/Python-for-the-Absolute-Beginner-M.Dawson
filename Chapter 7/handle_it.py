# program for handling excepts
# program runs till ends and inform us about mistakes

# using try instruction with except
# try takes particular slice of your code which probably can make a mistake

# to broad exception clause it need to be specify
try:
    num = float(input("Input number: "))
except:
    print("Some error occurs!")

# we can specify kind of mistake
# but this clause will not catch different mistake than inappropriate value and program will break
try:
    num = float(input("Input a number: "))
except ValueError:
    print("This is not a number!")

# taking multiple exceptions
# this part of code is trying to converse two different types into flaot number
print()
for value in (None, "Hej!"):
    try:
        print("Conversion try:", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Some error occurs!")

# using multiple excepts in different lines
print()
for value in (None, "Hi!"):
    try:
        print("Conversion try:", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("You can only change chain into numbers!")
    except ValueError:
        print("You can only converse chain of numbers!")

# using argument by adding as and name of variable

# take argument of exception
try:
    num = float(input("Input a number: "))
except ValueError as e:
    print("That wasn't a number, or in more python way ...")
    print(e)

# using else

# try / except / else
try:
    num = float(input("Input a number: "))
except ValueError as e:
    print("That wasn't a number!")
else:
    print("You have input number:", num)

input("\n\nFor closing program press enter.")
