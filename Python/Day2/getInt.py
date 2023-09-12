minvar = 1
maxvar = 100
attempts = 1


inputvar1 = int(input("Please type an integer between 1 and 100 : "))

while attempts < 3 :
	if inputvar1 > minvar and inputvar1 > maxvar :
		
		inputvar1 = int(input("Please type an integer between 1 and 100 : "))
		attempts = attempts + 1
	if attempts == 3:
		break
	
	elif inputvar1 < minvar and inputvar1 > maxvar :
		print(inputvar1)
print(None)