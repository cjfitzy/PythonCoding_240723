#exam1 = 50
#exam2 = 70
#exam3 = 60


#average_exam_markl = (exam1 + exam2 + exam3) /3
#print(average_exam_markl)


subject = input("Please enter a subject : ")
mark = int(input("Please marks for between 0 -100 : "))



#while 0 <= mark <= 100:
#	mathsexam = int(input("Please marks for Maths between 0 -100 : "))

i = 1

for loopvar in i > 0 :
    if (0 <= mark <= 100):
		print("Pass")
	else:
		i = i ++









#while True:
#	mathsexam = int(input("Please marks for Maths between 0 -100 : "))
#	if mathsexam >= 65:
#		print("Pass")
#	else:
#		print("Fail")
#	englishsexam = int(input("Please marks English between 0 -100 : "))
#	if englishsexam >= 65:
#		print("Pass")
#	else:
#		print("Fail")
#	ictsexam = int(input("Please marks for ICT between 0 -100 : "))
#	if ictsexam >= 65:
#		print("Pass")
#	else:
#		print("Fail")



## ExamAverage.py
## ExamAverage.py

## Function to input a valid exam mark between 0 and 100
##def input_valid_mark(subject):
##    while True:
##        mark = input(f"Enter the {subject} exam mark (0-100): ")
##        try:
##            mark = int(mark)
##            if 0 <= mark <= 100:
##                return mark
##            else:
##                print("Invalid mark. Please enter a mark between 0 and 100.")
##        except ValueError:
##            print("Invalid input. Please enter a valid integer.")

## Input exam marks
##math_mark = input_valid_mark("Math")
##english_mark = input_valid_mark("English")
##ict_mark = input_valid_mark("ICT")

## Calculate the average mark
##average_mark = (math_mark + english_mark + ict_mark) / 3

## Determine if the student passed or failed
##result = "Pass" if average_mark >= 65 else "Fail"

## Display the average mark and result
##print(f"Average mark: {average_mark:.2f}")
##print(f"Overall result: {result}")
