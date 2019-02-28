
class Student:
    
    def __init__(self, name, major, GPA, is_on_probation):
        self.name = name
        self.major = major
        self.GPA = GPA
        self.is_on_probation = is_on_probation

student1 = Student("John", "robot", 4.5, False)
student2 = Student("Jenny", "philosophy", 4, True)
print(student1.name)
print(student2.GPA)