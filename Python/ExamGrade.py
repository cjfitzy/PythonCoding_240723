
exam_mark =  input("Please enter your exam mark: ")


if int(exam_mark) < 1 or int(exam_mark) > 100:
    print("Error: marks must be between 1 and 100")
elif int(exam_mark) < 50:
    print("Fail")
elif int(exam_mark) >= 50 and int(exam_mark) < 60:
     print("Pass")
elif int(exam_mark) >= 61 and int(exam_mark) < 70:
    print("Merit")
elif int(exam_mark) >= 71 and int(exam_mark) < 100:
    print("Distinction")


