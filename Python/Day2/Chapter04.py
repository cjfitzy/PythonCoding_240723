
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
i = 0
print("lengh of ages")
print(len(ages))
print("put all ages on one line")
for loopvar in ages :
		print(loopvar)
		i += 1
print(" add one to each age")
#ages = [12,18,33]
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
i = 0
ages_plus_one = []

for loopvar in ages :
		print(loopvar +1)
		ages_plus_one.append(loopvar +1)
		i += 1
ages = ages_plus_one
print(ages)


print("remove ages < 16 > 65")
#ages = [12,18,33,84,45,67,12,82]
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
i = 0
for loopvar in ages :
	if loopvar > 65 or loopvar < 16 :
		print("remove age", loopvar )
		ages.remove(loopvar)
	else:
		i += 1
print(ages)


print("display count 16 -25")

#ages = [12,18,33,84,45,67,12,82,25,21,22]
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
i = 0

agecount = 0

for loopvar in ages:
	if loopvar > 16 and loopvar < 25 :
		agecount += 1

print(agecount)




print("sort the new ages ")
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,7,9,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

ages.sort()
print(ages)

print("what proportion of ages fall between 16 and 25 ")

total= len(ages)

agepercent = (agecount / len(ages)) * 100

print(agepercent)
