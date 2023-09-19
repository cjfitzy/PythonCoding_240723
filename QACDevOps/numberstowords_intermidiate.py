#code to take in a number and respond with the word
#123
#repsond with "one hundred and twenty three

###need to define the words eg #one #hundred #twenty #three


def num_to_words(num):
    ones = ["", "one", "two", "three", "four","five","six","seven","eight","nine"]


def convert(num_str):
    print(num_str)
    num_str = num_str.zfill(3)
    
    if num_str[0] >= 1:
        if num_str[1] == 0:
            print(num_str)
            return ones[int(num_str[0])]

                

num = 11
inttowords = num_to_words(num)

tet = convert(1)
print("test", tet)

