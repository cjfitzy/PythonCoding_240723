






###print("Hello World");


###varText = 'First Value in my List'
###intVar = 12345
###floatVar = 123.98
###stringVar = "30"
###boolVar = True

###list = [1, 2, 3]

###print(varText + " " + str(list[0]))


###print ("Then Loop Through my List")
###for item in list:
###    print(item)


###print("List all types" + " " + varText + " " + str(list[0]) + " " + "Then the rest" + " " + str(intVar) + " " + str(floatVar) + " " + str(stringVar) + " " + str(boolVar)+ " " + "the whole list" + " " + str(list))


###inputstring = input("Please type in a word: ")

###print("Print the String" + " " + inputstring )


###numVar1 = 15
###numVar2 = 23

###print(numVar1 + numVar2)

###print("Write both numbers out as a string" + " " + str(numVar1) + " and " + str(numVar2))

###print(numVar1 + int(stringVar))


###print(numVar1 , stringVar) # only converts to string

###print(int(floatVar)) # does not round up

###print(str(boolVar))
###print(int(boolVar)) 

###stringToBoolfalse = ""
###stringToBooltrue = "1"
###intToBooltrue = 234 #True
###intToBoolFalse = 0 #False

###floatToBoolFalse = 2.3 #True
###floatToBoolTrue = 0 #False


###print ("convert string int float to bool")
###print(bool(stringToBoolfalse)) 
###print(bool(stringToBooltrue)) # string with char always true, empty false
###print(bool(intToBooltrue)) 
###print(bool(intToBoolFalse)) 
###print(bool(floatToBoolFalse)) 
###print(bool(floatToBoolTrue)) 





###xstring = input("Please type a number: ")

###if int(xstring) <= 10:
###    print("Number is less than or equal to 10")

###elif int(xstring) > 10 and int(xstring) <20: #using and
###    print("Number is greater than 10 but less than 20 using and")
###else: 
###    print("Number is 20 or greater")


#### using an or
###if int(xstring) > 10 or int(xstring) <5:
###    print("Number is greater than 10 but less than 5 using or")

###print("Lets do some maths :)")

###calNumber1 = input("Please type first number: ")
###calNumber2 =  input("Please type second number: ")
###calNumber3 =  input("Please type third number: ")



###print("do some calculations with 1st/2nd numbers")

###timesNumbers = int(calNumber1) * int(calNumber2) 
###divNumbers = int (calNumber1) / int(calNumber2)
###addNumbers = int (calNumber1) - int(calNumber2)
###subNumbers = int (calNumber1) + int(calNumber2)


###print(timesNumbers)
###print(divNumbers)
###print(addNumbers)
###print(subNumbers)


###if int (calNumber1) % int(calNumber2) != 0:
###     print(calNumber1, "does not divide evenly by", calNumber2 )
###else:
###    print(calNumber1, "divides evenly by", calNumber2 )


###print("compare the three numbers to find out the biggest")

###if int(calNumber1) >= int(calNumber2) and int(calNumber1) >=int(calNumber3):
###    print("the first number", calNumber1, "is the biggest number")
###elif int(calNumber2)>= int(calNumber1) and int(calNumber2)>= int(calNumber3):
###    print("the second number", calNumber2, "is the biggest number")
###else:
###    print("the third number", calNumber3, "is the biggest number")


###if int(calNumber1) < 1000:
###       if int(calNumber1) < 100:
###           if int(calNumber1) < 10:
###               print("you have a single digit number")
###           else:
###               print("you have a double digit number")
###       else:
###           print("you have a three digit number")
###else:
###    print("you have a giant number")
        


###print(type(calNumber1))



###while loops are usefull if you dont know how many iterations something will take
    
##x = 1

##while x < 5:
##    print(x, "Hello World")
##    x = x + 1    #x += 1


##n = 1
##while n <= 5:
##    print('*' * n)
##    n = n +1
##while n > 0:
##    n = n-1
##    print('*' * n)


##inputvar1 = int(input("type in a number:"))
##while inputvar1 >= 1:
##    print(inputvar1)
##    inputvar1= inputvar1 -1
##    if inputvar1 == 13:
##            break

##  # continue  





  
##inputvar1 = int(input("type in a number:"))
##while inputvar1 >= 0:
##    print(inputvar1)
##    inputvar1= inputvar1 -1
##    if inputvar1 == 13:
##            continue




##print(range(10))
###help(range(10))



##for loopvar1 in range(4): # 0 1 2 3
##    print(loopvar1)
##print("------------")
##for loopvar1 in range (2,7): #2,3,4,5,6
##    print(loopvar1)
##print("------------")
##for loopvar1 in range(10,0,-1): # 10,9,8,7,6,
##    print(loopvar1)
##print("------------")
##for loopvar1 in range(0,100,5): # 0,5,10,...95
##    print(loopvar1)
##print("------------")

##for loopvar1 in range(0,100,5): # 0,5,10,...95
##    if loopvar1 == 50:
##        break
##    print(loopvar1)
##print("------------")


#####list






#stringvar = "leon is ace"

#for letter in stringvar:
#    print(letter)


#print(len(stringvar)) # how many items in the list
#print(stringvar[3]) #single charc
#print(stringvar[0:4]) # range of letters

#shoppinglist = [ 'fish', 'cat', 'dog']

#boollist = [True, False, True, True, True, False]
    

#shoppinglist.append("plasters")

#print(shoppinglist)

#print(boollist.count(True)) # count how many of specific item is in thelist

#shoppinglist.remove("plasters")

#shoppinglist.insert(0, 'freddos')

#shoppinglist.sort()


## spilt # join

##coverting list to string


#joinchar = ","
#shoppingliststring = joinchar.join(shoppinglist)

#print(shoppingliststring)
#print(type(shoppingliststring))

##converting string to list vs versa




#splitstr = "mointor,laptop,ipad,mouse,keyboard,webcam"

#newlist1 = splitstr.split(",")
#print(newlist1)
#print(type(newlist1))





#from string import capwords 

#somewords = input("type something")
#print(capwords(somewords))


#from calendar import monthcalendar as mnth

#for row in mnth(2023,9):
#    print(row)


inputvar1 = input("no1: ")
inputvar2 = input("no2: ")

if inputvar1.isnumeric():
    if inputvar2.isnumeric():
        print(float(inputvar1)+float(inputvar2))
    else:
        print("Numbers Only")
else:
    print("Numbers Only")


    
if inputvar1.isnumeric() and inputvar2.isnumeric() :
        print(float(inputvar1)+float(inputvar2))
else:
    print("Numbers Only")
