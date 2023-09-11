print("Pythagoras’ Calculator" )
print("1. Find the length of A given B and C " )
print("2. Find the length of B given A and C " )
print("3. Find the length of C given A and B " )


selection = input("Which calculation: ")



if int(selection) == 1:
    value_B =  input("Select a value for B: ")
    value_C =  input("Select a value for C: ")
    print("The length of A given that  C=", int(value_B), "and B=", int(value_C), "then A =")
elif int(selection) == 2:
    value_A =  input("Select a value for A: ")
    value_C =  input("Select a value for C: ")
    print("The length of B given that  A=", int(value_A), "and C=", int(value_C), "then B =")
elif int(selection) == 3:
    value_A =  input("Select a value for A: ")
    value_B =  input("Select a value for B: ")
    print("The length of C given that  A=", int(value_A), "and B=", int(value_B), "then A =")