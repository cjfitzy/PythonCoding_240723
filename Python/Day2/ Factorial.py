
inputvar1 = int(input("Please type an integer: "))
fact = 1

while inputvar1 > 0 :
    fact = fact * inputvar1
    inputvar1 =  inputvar1 - 1
 
print(fact)




for loopvar in range (1, inputvar1 + 1):
    fact = loopvar * fact
print(fact)