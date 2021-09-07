# Program showing how to save text into txt file

print("Create txt file using write().\n")
text_file = open("save_it.txt", "w")

# if I don't use \n all content would be in one row
text_file.write("Row 1.\n")
text_file.write("This is row 2.\n")
text_file.write("This row is row 3.\n")

text_file.close()

print("Showing the content of our new txt file.\n")
text_file = open("save_it.txt", "r")
print(text_file.read())
text_file.close()

# saving file using writelines()
# when we create the same file again the content is erased

text_file = open("save_it.txt", "w")

# I create list lines
lines = ["Row 1.\n",
         "This is row 2.\n",
         "This row is row 3.\n"]

text_file.writelines(lines)
text_file.close()

text_file = open("save_it.txt", "r")

# print as list
print(text_file.readlines())
text_file.close()

# to read the content again I need to close and open that file
# because python remember what I read and show empty lines
text_file = open("save_it.txt", "r")
print(text_file.read())

text_file.close()
