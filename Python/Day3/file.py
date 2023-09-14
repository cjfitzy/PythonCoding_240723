carsales = open("Python/Day3/carSale.csv")



header = carsales.readline()
lines = carsales.readlines()


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
    TotalSales = (str(words[0]), ("Total yearly Sales"), int(words[1]) + int(words[2]) + int(words[3]) + int(words[4]) + int(words[5]) + int(words[6]) + int(words[7]) + int(words[8]))
    print(TotalSales)
    sales.append(words[1]+ words[2])
print("Jan 2019 Total =", janTotal,"Feb 2019 Total =", febTotal, "March 2019 Total =", marchTotal,"April 2019 Total =", aprTotal,"May 2019 Total =", mayTotal,"June 2019 Total =", juneTotal,"July 2019 Total =", julyTotal,"August 2019 Total =", augTotal )
print("Grand Total",janTotal +  febTotal + marchTotal + aprTotal + mayTotal + juneTotal + julyTotal + augTotal  )




print("---------------------------Other way------------------- ")
companies = []
sales = [] 

header = carsales.readline()
lines = carsales.readlines()

for line in lines:
    parts = line.split(',')
    company = parts[0]    
    companies.append(company)    
    salenumbers = [int(s) for s in parts[1:]]
    sales.append(salenumbers)


i = 0
janTotal = 0
febTotal = 0
marchTotal = 0
aprTotal = 0
mayTotal = 0
juneTotal = 0
julyTotal = 0
augTotal = 0
TotalSales = 0

for item in sales:
    itemtotal = sum(item)
    janTotal += int(item[0])
    febTotal += int(item[1])
    marchTotal += int(item[2])
    aprTotal += int(item[3])
    mayTotal += int(item[4])
    juneTotal += int(item[5])
    julyTotal += int(item[6])
    augTotal += int(item[7])
    print(companies[i],"Yearly Total:", itemtotal)
    i += 1
print(janTotal)
print(febTotal)
print(marchTotal)
print(aprTotal)
print(mayTotal)
print(juneTotal)
print(julyTotal)
print(augTotal)
print("Total:",janTotal + febTotal + marchTotal + aprTotal + mayTotal + juneTotal + julyTotal + augTotal )




