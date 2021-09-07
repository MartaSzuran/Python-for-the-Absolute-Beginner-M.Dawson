# program for pickling data

# demonstrate how to pickle and put data on shelve
# we can pickle : number, string, tuple, list, dictionaries

import pickle, shelve
# pickle module let us to save and keep data in file
# shelve module let us storage pickle object and give us access to it

print("Pickle list.\n")

# create lists
variety = ["mild", "spicy", "sour"]
shape = ["whole", "cut along", "cut into slices"]
brand = ["Dawton", "Klimex", "Vortumnus"]

# open new passive file for pickle list
f = open("pickle1.dat", "wb")

# storage 3 lists with pickle.dump()

pickle.dump(variety, f)
pickle.dump(shape, f)
pickle.dump(brand, f)
f.close()

# reading content from file and unpickle

print("Unpickle list.\n")
f = open("pickle1.dat", "rb")
variety = pickle.load(f)
shape = pickle.load(f)
brand = pickle.load(f)

print(variety)
print(shape)
print(brand)
f.close()

# using shelve for storage lists in one file

# creating shelve

print("\nPutting lists on shelve using shelve.open() - (it pickle objects not characters).\n")
# variable s is dictionary
s = shelve.open("pickle2.dat")

# add 3 lists to shelve
# variety is a key and ["mild", "spicy", "sour"] is value
# key can be only a chain of characters
s["variety"] = ["mild", "spicy", "sour"]
s["shape"] = ["whole", "cut along", "cut into slices"]
s["brand"] = ["Dawton", "Klimex", "Vortumnus"]

# making sure that lists are saved using sync()
# shelve is also updating using close()
# shelve module is using memory more efficient
s.sync()

print("\nDownloading lists from shelve file:\n")
print("brand -", s["brand"])
print("shape -", s["shape"])
print("variety -", s["variety"])
s.close()

input("\nFor closing the file press Enter.")
