import math

print("Pythagoras Calculator" )
print("1. Find the length of A given B and C " )
print("2. Find the length of B given A and C " )
print("3. Find the length of C given A and B " )


selection = input("Which calculation: ")




if int(selection) == 1:
    value_B =  input("Select a value for B: ")
    value_C =  input("Select a value for C: ")
    value_A_squared = (int(value_B)**2) + (int(value_C) **2)
    print("The length of A sqaured given that B Squared =", (int(value_B)**2), "and C Squared =", (int(value_C)**2), "then A Squared =", value_A_squared)
    print("The length of Side A equals ", math.sqrt(value_A_squared))
elif int(selection) == 2:
    value_A =  input("Select a value for A: ")
    value_C =  input("Select a value for C: ")
    value_B_squared = (int(value_A)**2) + (int(value_C) **2)
    print("The length of B sqaured given that A square =", (int(value_A)**2), "and C sqaured =", (int(value_C)**2), "then B sqaured =", value_B_squared)
    print("The length of Side B equals ", math.sqrt(value_B_squared))
elif int(selection) == 3:
    value_A =  input("Select a value for A: ")
    value_B =  input("Select a value for B: ")
    value_C_squared = (int(value_A)**2) + (int(value_B) **2)
    print("The length of C sqaured given that A square =", (int(value_A)**2), "and B sqaured =", (int(value_B)**2), "then C sqaured =", value_C_squared)
    print("The length of Side B equals ", math.sqrt(value_C_squared))