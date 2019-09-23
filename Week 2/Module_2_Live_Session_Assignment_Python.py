"""Name of Activity: Module 2 Live Session Assignment:
Python
Name: John Carpenter
ID: jcm7dt
Partner: Nathan England
ID: nle4bz
"""
class Student:
# fields: name, id, grades(a list)
# #Local variable
# #grades = [] # initially empty
    def __init__(self, name, id):
    # constructor
        self.name = name
        self.id = id
        self.grades = [] #creates a new empty list for each student
    def addGrade(self, grade): # add the grade to the list of grades
        self.grades.append(grade)

    def showGrades(self): # displaying the grades
        grds = '' # empty string
        for grade in self.grades: # Loop through grades list
            grds += str(grade) + ' '  # assign each grade to the string grds
        return grds

    def average(self): # takes average of grades
        return str(sum(self.grades)/len(self.grades))

    def __str__(self):
        return self.name + ', ' + self.id + '\n' + 'Grades: ' + self.showGrades() + '\n' + 'Average: ' + self.average()

StudentA = Student('John' , '123')
print(str(StudentA.name) + ', ' + str(StudentA.id))
StudentA.addGrade(90)
StudentA.addGrade(95)
StudentA.addGrade(100)
print("Grade: " , StudentA.showGrades())
print("Average: " , StudentA.average())
print(StudentA)

StudentB = Student('Nathan' , '456')
print(str(StudentB.name) + ', ' + str(StudentA.id))
StudentB.addGrade(91)
StudentB.addGrade(96)
StudentB.addGrade(101)
print("Grade: " , StudentB.showGrades())
print("Average: " , StudentB.average())
print(StudentB)