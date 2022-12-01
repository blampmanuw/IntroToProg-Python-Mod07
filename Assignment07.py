# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description:  Pickling, Exception Handling
# ChangeLog (Who,When,What):
# BLampman 11.30.2022, Created to complete assignment 07
# ---------------------------------------------------------------------------- #


import pickle  # This imports code from another code file

# intID = int(input("Enter ID: "))
while True:
    try:
        intID = int(input("Please enter an ID: "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
strName = str(input("Enter Name: "))
lstCustomer = [intID, strName]
print(lstCustomer)

# Store the data with the pickle.dump method
objFile = open("AppData.dat", "ab")
pickle.dump(lstCustomer, objFile)
objFile.close()

# Read the data back with the pickle.load method
objFile = open("AppData.dat", "rb")
objFileData = pickle.load(objFile) #load() only loads one row of data.
objFile.close()

print(objFileData)

#
# try:
#     quotient = 13/0
#     print(quotient)
# except Exception as e:
#     print("There was an error! << Custom Message")
#
#     print("Built-In Pythons error info: ")
#     print(e)
#     print(type(e))
#     print(e.__doc__)
#     print(e.__str__())

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was not a valid number.  Try again...")
#
#




