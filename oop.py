# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

# def average(sequence):
#     return sum(sequence) / len(sequence)

# print(average(student["grades"]))
# print(student.average())

##############################

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        return sum(self.grades) / len(self.grades)

student = Student("Bob", (100, 100, 100, 70, 65))
student1 = Student("Rolf", (100, 100, 80, 80, 85))

# print(student.name)
#print(Student.average(student))
print(student.average())
print(student1.average())