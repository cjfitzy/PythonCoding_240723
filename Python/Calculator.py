calNumber1 = input("Please type first number: ")
calNumber2 =  input("Please type second number: ")

print("Please choose which number you wish for the operation to perform")

print("1    Add        +" )
print("2    Subtract   -" )
print("3    Multiply   *" )
print("4    Divde      /" )
print("5    Square     S" )


operation = input("Operation number:")






if int(operation) == 1:
    print("Value =", int(calNumber1) + int(calNumber2))
elif int(operation) == 2:
    print("Value =", int(calNumber1) - int(calNumber2))
elif int(operation) == 3:
    print("Value =", int(calNumber1) * int(calNumber2))
elif int(operation) == 4:
    print("Value =", int(calNumber1) / int(calNumber2))
else:
    print("Value =", int(calNumber1) ** int(calNumber2))