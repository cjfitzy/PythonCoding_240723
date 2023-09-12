#investment = 100
#i = 0
#while investment < 1000 :
#	investment == investment * 1.1
#	print (investment)
#	i = i + 1
	
#print(i)



investment = 100
target = 1000
interestrate = 10
i = 0
while investment < target :
	investment = investment + ((investment / 100) * interestrate)
	i = i + 1
	print (investment)
print(i)