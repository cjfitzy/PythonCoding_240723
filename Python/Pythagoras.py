print("Pythagoras Calculator" )
print("1. Find the length of A given B and C " )
print("2. Find the length of B given A and C " )
print("3. Find the length of C given A and B " )


selection = input("Which calculation: ")



if int(selection) == 1:
    value_B =  input("Select a value for B: ")
    value_C =  input("Select a value for C: ")
    print("The length of A sqaured given that  B=", int(value_B), "and C=", int(value_C), "then A =", (int(value_B)**2) + (int(value_C) **2))
    print("Square root of A Square equals")
elif int(selection) == 2:
    value_A =  input("Select a value for A: ")
    value_C =  input("Select a value for C: ")
    print("The length of B sqaured given that  A=", int(value_A), "and C=", int(value_C), "then B =", (int(value_A)**2) + (int(value_C) **2))
    print("Square root of B Square equals")
elif int(selection) == 3:
    value_A =  input("Select a value for A: ")
    value_B =  input("Select a value for B: ")
    print("The length of C sqaured given that  A=", int(value_A), "and B=", int(value_B), "then C =", (int(value_A)**2) + (int(value_B) **2))
    print("Square root of C Square equals")