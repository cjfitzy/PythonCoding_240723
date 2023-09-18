import random
class Dice:

    def __init__(self,sides):
        self.sides = sides
        
        
    def roll(self):
        return random.randint(1,self.sides)


D2 = Dice(2)
D4 = Dice(4)
D6 = Dice(6)
D20 = Dice(20)

print("random role for D2",D20.roll())



#LetterCheck("vowels").isItAVowel("C")
        
 
#print(LetterCheck("vowels").isItAVowel("C"))



##character_sheet
##name
##class
##level
##race
##alignment
## hit point
## armor class
