class LetterCheck:
    def __init__(self,lettergroup):
        self.lettergroup = lettergroup.upper()
        self.vowels = "AEIOU" 
        
    def isItAVowel (self,letter):
       if letter.upper() in self.vowels:
           return True
       else:
           return False



LetterCheck("vowels").isItAVowel("C")
        
 
print(LetterCheck("vowels").isItAVowel("C"))