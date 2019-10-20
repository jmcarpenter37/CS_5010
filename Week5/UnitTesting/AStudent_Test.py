# ID: jmc7dt
# Assignment: HW 5 Unit Testing
# This script tests the AStudent_Class file
import unittest
from AStudent_Class import *

# Begin testing here
class AStudent_Testing(unittest.TestCase):
    def test_AddGrade(self):
        Student1 = AStudent("John", "123456789", 0)
        Student1.enrollInCourse("Fourier Analyis and Wavelets")
        Student1.addGrade(99) # Adding a grade of 99 to an otherwise empty list of grades as stated in the AStudent_Class
        self.assertEqual(Student1.grades[0], 99) # The reson I indexed on zero here is because Student1.grades returns an arrray of grades added. In which case [99] != 99
        # As we can see, the addGrade method added the grade of 99 to the otherwise empty array!

    def test_Average(self):
        Student1 = AStudent("John", "123456789", 0)
        Student1.enrollInCourse("Fourier Analyis and Wavelets")
        Student1.addGrade(99) # Add a first grade of 99
        Student1.addGrade(100) # Add a second grade of 100
        # We know the average of 99 and 100 is 99.5 so we test that below
        self.assertEqual(Student1.average() , 99.5)


if __name__ == '__main__':
    unittest.main()


