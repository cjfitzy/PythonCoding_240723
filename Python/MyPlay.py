

from ctypes.wintypes import BOOL
from tkinter import StringVar


print("Hello World");


varText = 'First Value in my List'
intVar = 12345
floatVar = 123.98
stringVar = "30"
boolVar = True

list = [1, 2, 3]

print(varText + " " + str(list[0]))


print ("Then Loop Through my List")
for item in list:
    print(item)


print("List all types" + " " + varText + " " + str(list[0]) + " " + "Then the rest" + " " + str(intVar) + " " + str(floatVar) + " " + str(stringVar) + " " + str(boolVar)+ " " + "the whole list" + " " + str(list))


inputstring = input("Please type in a word: ")

print("Print the String" + " " + inputstring )


numVar1 = 15
numVar2 = 23

print(numVar1 + numVar2)

print("Write both numbers out as a string" + " " + str(numVar1) + " and " + str(numVar2))

print(numVar1 + int(stringVar))


print(numVar1 , stringVar) # only converts to string

print(int(floatVar)) # does not round up

print(str(boolVar))
print(int(boolVar)) 

stringToBoolfalse = ""
stringToBooltrue = "1"
intToBooltrue = 234 #True
intToBoolFalse = 0 #False

floatToBoolFalse = 2.3 #True
floatToBoolTrue = 0 #False


print ("convert string int float to bool")
print(bool(stringToBoolfalse)) 
print(bool(stringToBooltrue)) # string with char always true, empty false
print(bool(intToBooltrue)) 
print(bool(intToBoolFalse)) 
print(bool(floatToBoolFalse)) 
print(bool(floatToBoolTrue)) 
