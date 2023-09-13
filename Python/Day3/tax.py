

personal_allowance = 11850
low_tax_bracket_amount = 34500
low_tax_bracket_percent = 0.2
mid_tax_bracket_amount = 150000
mid_tax_bracket_percent = 0.4
high_tax_bracket_percent = 0.45




def getIncomeTax(salary):

    if salary <= personal_allowance:
        return "No Tax to be paid"

    elif  salary <= low_tax_bracket_amount:

          lowtax = salary - personal_allowance
          lowtaxamount = lowtax * low_tax_bracket_percent
          return ("Total Tax to be paid",round((lowtaxamount),2))

    elif salary <= mid_tax_bracket_amount:

        midtax = salary - low_tax_bracket_amount +1
        midtaxamount = midtax * mid_tax_bracket_percent

        lowtaxamount = (low_tax_bracket_amount - personal_allowance)  * low_tax_bracket_percent

        return ("Total Tax to be paid",round((midtaxamount+lowtaxamount),2))
    else:
        hightax = salary - mid_tax_bracket_amount + 1
        hightaxamount = hightax * high_tax_bracket_percent

        midtaxamount = (mid_tax_bracket_amount - low_tax_bracket_amount)  * mid_tax_bracket_percent

        lowtaxamount = (low_tax_bracket_amount - personal_allowance)  * low_tax_bracket_percent

        return ("Total Tax to be paid",round((hightaxamount+midtaxamount+lowtaxamount),2))


salary = int(input("Please enter your salary: "))

getIncomeTax(salary)
print(getIncomeTax(salary))




#50 - 34500 = 15500 * 0.4 = 6200 + (34500 - 11850 = 22650 * 0.2 = 4530)  = 10730

#(15000 - 34500 = 115500 * 0.40 = 46200) + (34500 - 11850 = 22650 * 0.2 = 4530)
#50730

#160000 - 150001 = (10 000 * 0.45 = 4500 ) + ( 15000 - 34500 = 115500 * 0.40 = 46200) + (34500 - 11850 = 22650 * 0.2 = 4530)
# = 4500 + 46200 + 4530 =  55230


