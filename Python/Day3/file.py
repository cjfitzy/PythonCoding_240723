#from dataclasses import dataclass


#fileobjectvar = open("Python/Day3/Readme.md")

#print(type(fileobjectvar))
#stringvar = fileobjectvar.read()
#print(stringvar)

#print("how many sheep in the file")
#print(stringvar.count("sheep"))



#dogstory = stringvar.replace("sheep", "dog")
#print(dogstory)

#fileobjectvar.seek(0)

#listvar1 = fileobjectvar.readlines()
#print(listvar1[2])  # graps a line 

#listvar1.append("THE END\n")
#print(listvar1)


#fileobjectvar.close()

#writefileobjectvar = open("Python/Day3/Readme.md","w") # open and delete file contents

##push the data to be written to disk
#writefileobjectvar.write(dogstory)
#writefileobjectvar.close()


##basic work
##open()
##read() or readline()
##close()
##manipulate the dataclass
##open("w")
##write()
##close()

carsales = open("Python/Day3/carSale.csv")



header = carsales.readline()
lines = carsales.readlines()
print(header)

janTotal = 0
febTotal = 0
marchTotal = 0
aprTotal = 0
mayTotal = 0
juneTotal = 0
julyTotal = 0
augTotal = 0
TotalSales = 0
sales = []
for line in lines:
    words = line.split(",")
    #print(words[1])
    janTotal += int(words[1])
    febTotal += int(words[2])
    marchTotal += int(words[3])
    aprTotal += int(words[4])
    mayTotal += int(words[5])
    juneTotal += int(words[6])
    julyTotal += int(words[7])
    augTotal += int(words[8])
   # TotalSales = (str(words[0]), ("Total yearly Sales"), int(words[1]) + int(words[2]) + int(words[3]) + int(words[4]) + int(words[5]) + int(words[6]) + int(words[7]) + int(words[8]))
    #print(TotalSales)
    sales.append(words[1]+ words[2])
    print(sales)
print("Jan 2019 Total =", janTotal,"Feb 2019 Total =", febTotal, "March 2019 Total =", marchTotal,"April 2019 Total =", aprTotal,"May 2019 Total =", mayTotal,"June 2019 Total =", juneTotal,"July 2019 Total =", julyTotal,"August 2019 Total =", augTotal )
print(janTotal +  febTotal + marchTotal + aprTotal + mayTotal + juneTotal + julyTotal + augTotal  )


#####

#companies = []
#sales = [] 

#header = carsales.readline()
#lines = carsales.readlines()

##for line in lines:
##    words1 = line.strip().split(",")
##    sales.append(list(map(int,words1[1])))

##print(sales)


##for line in lines:
##    words = line.split(",")
##    print(words[1])
##    companies.append(words[0])
##    data = line.strip().split(',') 
##    sales.append(list(map(int,data)))
##    print(sales)
#for line in lines:
#    for x in range(0, len(lines),2): 
#        data = line.strip().split(',') 
#        sales.append(list(map(int,data)))
#        print(sales)

