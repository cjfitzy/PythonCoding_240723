class Student:
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom
        self.testscore = []

    def add_test_score (self,score):
        self.testscore.append(score)

    def cal_average_score(self):
        return sum(self.testscore) / len(self.testscore)



student1 = Student("Claire",30, "DevOps")
student1.add_test_score(99)
student1.add_test_score(98)
student1.add_test_score(97)

average_score = student1.cal_average_score()


print(student1.name , student1.age, student1.testscore, average_score)

