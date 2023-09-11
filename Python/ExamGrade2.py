student_level = input("Please enter your level: ")
exam_mark =  input("Please enter your exam mark: ")



if int(student_level) == 1:
    if int(exam_mark) >= 1 and int(exam_mark) <= 100:
        if int(exam_mark) >= 50:
            if int(exam_mark) >= 50 and int(exam_mark) <= 60:
                print("Pass")
            elif int(exam_mark) >= 61 and int(exam_mark) <= 60:
               print("Merit")
            elif int(exam_mark) >= 71 and int(exam_mark) <= 100:
               print("Distinction")
        else:
            print("Fail")
    else:
        print("Error: marks must be between 1 and 100")
else:
    if int(exam_mark) >= 1 and int(exam_mark) <= 100:
        if int(exam_mark) >= 40:
            if int(exam_mark) >= 40 and int(exam_mark) <= 50:
                print("Pass")
            elif int(exam_mark) >= 51 and int(exam_mark) <= 65:
               print("Merit")
            elif int(exam_mark) >= 66 and int(exam_mark) <= 100:
               print("Distinction")
        else:
            print("Fail")
    else:
        print("Error: marks must be between 1 and 100")