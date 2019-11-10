"""
Name of Activity: Module 3 Live Session Assignment: Class Inheritance
Name: Nathan England
Computing ID: nle4bz

Partner: John Carpenter
Partner Computing ID: jmc7dt
"""

class Student:
    # fields: name, id, grades(a list)
    
    #Local variable
    #grades = [] # initially empty
    
    def __init__(self, name, id):  # constructor
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
        num = sum(self.grades)
        denom = len(self.grades)
        return str(num/denom)
    
     #1. Add two methods to class Student
    def welcome(self, graduationyear): # first new method
        print("Welcome " + self.name + " to the class of " + str(graduationyear))
    
    def graduated(self, currentyear, graduationyear): # second new method
        if currentyear > graduationyear:
            return True
        else:
            return False
        
    def __str__(self):
        return self.name + ', ' + self.id + '\n' + 'Grades: ' + self.showGrades() + '\n' + 'Average: ' + self.average()
    
    #2. Class that inherits one or two of these methods
class Freshman(Student): #child class of student
    def __init__(self, name, id, graduationyear):  # Note all the attributes
        Student.__init__(self, name, id) # Call the base class constructor
        self.graduationyear = graduationyear
        
    def __str__(self):
      retStr = Student.__str__(self) # Call to-string of base class (Student)
      retStr += '\n Graduation Year: ' + str(self.graduationyear)
      return retStr
  
    #Testing inheritance
freshman1 = Freshman('Nathan', '456', 2018)
print(freshman1.welcome(freshman1.graduationyear))
print(freshman1.graduated(2019, freshman1.graduationyear))

#==================================================
    
student1 = Student('Jones', '123')
print(str(student1.name) + ', ' + str(student1.id)) # Output: Jones, 123
student1.addGrade(88)
student1.addGrade(72)
student1.addGrade(100)
print("Grades: " + student1.showGrades()) # showing grades for student1
# print(student1) # Will NOT work, since we do not have a "to-string" (__str__) method
# Output of the above line will be a memory address like:
#      <__main__.Student object at 0x00000220B8611BE0>
#==================================================

# ** TO THINK ABOUT: **
# This is fine, however, what happens if you create a second Student object??
# Local ("global") variable grades (a list - which is a mutable object) will
# accumulate grades from ALL students... this behavior is not what we want. 
# Uncomment lines 46-51 below and see what happens.  How would you fix this?? 
# For now, the above file is fine for the above scenario. 

# =============================================================================
s2 = Student('Clayton', '115')
print(str(s2.name) + ', ' + str(s2.id)) 
s2.addGrade(85)
s2.addGrade(95)
s2.addGrade(99)
print("Grades: " + s2.showGrades())  # !!!
# =============================================================================

#3: Creating Student 1 and adding grades appears to have desired outcome by printing student name and ID and allowing you to add grades to the grades list.
#When creating s2 the code prints the individual student's name and ID, but s2's grades output includes those of Student 1 which is not the desired outcome.

#4: Defined grades within the constructor so that a new empty grades list is created for each student (see changed code above).

#5: See above __str__(self) function (lines 35-36)

#6:  See above average(self) function (lines 30-33)

#7:
studentA = Student('John', '123')
print(str(studentA.name) + ', ' + str(studentA.id)) # Output: John, 123
studentA.addGrade(90)
studentA.addGrade(95)
studentA.addGrade(100)
print("Grades: " + studentA.showGrades()) # showing grades for studentA
print("Average: " + studentA.average())
print(studentA) # Will work, since we do have a "to-string" (__str__) method

studentB = Student('Nathan', '456')
print(str(studentB.name) + ', ' + str(studentB.id)) # Output: Nathan, 456
studentB.addGrade(91)
studentB.addGrade(96)
studentB.addGrade(101) # Test had bonus questions
print("Grades: " + studentB.showGrades()) # showing grades for studentB
print("Average: " + studentB.average())
print(studentB) # Will work, since we do have a "to-string" (__str__) method

