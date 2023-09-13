varstring= " this is a lovely string of mine"
vowlcount = 0



for letter in varstring:
    if letter.count("a") or letter.count("e") or letter.count("i") or letter.count("o") or letter.count("u"):
        vowlcount += 1 
print(vowlcount)


for letter in varstring:
    if letter.upper in ["AEIOU"]:
        vowlcount += 1 
print(vowlcount)