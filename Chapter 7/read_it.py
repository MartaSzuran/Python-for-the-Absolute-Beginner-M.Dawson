# reading text files
# examples

print("Open and close file.")
text_file = open("read_it.txt", "r")
text_file.close()

print("Read characters from file.")
text_file = open("read_it.txt", "r")
print(text_file.read(1))
print(text_file.read(7))

print("Read whole at once.")
text_file = open("read_it.txt", "r")
whole_thing = text_file.read()
print(whole_thing)
text_file.close()

print("Read character from row.")
text_file = open("read_it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(7))
text_file.close()

print("Read one row at time.")
text_file = open("read_it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("Read whole text to list.")
text_file = open("read_it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("Download content from whole text row by row using loop.")
text_file = open("read_it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

input("\n\nFor closing program press enter.")