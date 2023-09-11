age = input("Please type in you age: ")


if int(age) >= 18:
    print("You are in category A")

if int(age) >= 16 and int(age) < 18:
    print("You are in category B")

if int(age) < 16:
    print("You are in category C")


if int(age) >= 18:
    print("You are in category A")
elif int(age) >= 16 and int(age) <18: 
    print("You are in category B")
else: 
    print("You are in category C")

