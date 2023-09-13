class Grade:
    WEIGHT_MIDTERM = 0.3
    WEIGHT_FINAL = 0.2
    WEIGHT_HOMEWORK = 0.5
    def __init__(self, midterm, final, homework):
        self.midterm = midterm
        self.final = final
        self.homework = homework
    
    def calculate_grade(self):
        return self.midterm * Grade.WEIGHT_MIDTERM + self.final * Grade.WEIGHT_FINAL + self.homework * Grade.WEIGHT_HOMEWORK

    def __str__(self):
        return f"weight_midterm: {Grade.WEIGHT_MIDTERM}, weight_final: {Grade.WEIGHT_FINAL}, weight_homework: {Grade.WEIGHT_HOMEWORK}, midterm: {self.midterm}, final: {self.final}, homework: {self.homework}"
    


# Test with small numbers
grade = Grade(3.5, 5.0, 2.0)
print(f"Grade object using __str__() function: {grade}")

# Get one class and one instance attribute using the dot "." operator
print("\nGet one class and one instance attribute using the dot \".\" operator")
print("Class attribute weight_midterm:", Grade.WEIGHT_MIDTERM)
print("Instance attribute midterm:", grade.midterm)
print(f"The content of the grade object with vars is {vars(grade)}")
print(f"Grade object using __str__() function: {grade}")
# The "." operator gets the value of the instance attribute and the class attribute

# Change one class and one instance attribute using the dot "." operator
print("\nChange one class and one instance attribute using the dot \".\" operator")
Grade.WEIGHT_MIDTERM = 0.4
grade.midterm = 4.0
print(f"The content of the grade object with vars is {vars(grade)}")
print(f"Grade object using __str__() function: {grade}")
# The "." operator changes the value of the instance attribute and the class attribute

# Get one class and one instance attribute using the getattr() function
print("\nGet one class and one instance attribute using the getattr() function")
print("Class attribute weight_midterm:", getattr(Grade, "weight_midterm"))
print("Instance attribute midterm:", getattr(grade, "midterm"))
print(f"The content of the grade object with vars is {vars(grade)}")
print(f"Grade object using __str__() function: {grade}")
# The getattr() function gets the value of the instance attribute and the class attribute

# Change one class and one instance attribute using the setattr() function
print("\nChange one class and one instance attribute using the setattr() function")
setattr(Grade, "weight_midterm", 0.5)
setattr(grade, "midterm", 4.5)
print(f"The content of the grade object with vars is {vars(grade)}")
print(f"Grade object using __str__() function: {grade}")
# The setattr() function changes the value of the instance attribute and the class attribute

# Delete one class and one instance attribute using the delattr() from an object
# Is it always possible to do this?
print("\nDelete one class and one instance attribute using the delattr() from and object")
delattr(grade, "midterm")
print(f"The content of the grade object after deleting instance attribute weight_midterm with vars is {vars(grade)}")
# delattr(grade, "Grade.weight_midterm")
# print(f"The content of the grade object after deleting class attribute Grade.weight_midterm with vars is {vars(grade)}")
# print(f"Grade object using __str__() function: {grade}")
# An error occurs when trying to delete a class attribute from an object using delattr() function
# It is not possible to delete a class attribute from an object using delattr() function

# Delete one class and one instance attribute using the delattr() from a class
# Is it always possible to do this?
print("\nDelete one class and one instance attribute using the delattr() from a class")
delattr(Grade, "weight_homework")
print(f"The content of the grade object after deleting class attribute weight_midterm with vars is {vars(grade)}")
# delattr(Grade, "homework")
print(f"The content of the grade object after deleting instance attribute midterm with vars is {vars(grade)}")
# print(f"Grade object using __str__() function: {grade}")
# An error occurs when trying to delete an instance attribute from a class using delattr() function
# It is not possible to delete an instance attribute from a class using delattr() function


# Create an object and delete the object. Create another object and check is there
print("\nCreate an object and delete the object. Create another object and check is there")
grade = Grade(3.5, 5.0, 2.0)
print(f"The content of first grade object with vars is {vars(grade)}")
del grade
grade = Grade(3.0, 3.0, 3.0)
print(f"The content of second grade object with vars is {vars(grade)}")
# print(f"Grade object using __str__() function: {grade}")
# The second object is created and the first object is deleted

# Delete the class and try to create a new object from the class. Explain if there is an error.
print("\nDelete the class and try to create a new object from the class. Explain if there is an error.")    
del Grade
grade = Grade(3.5, 3.5, 3.5)
print(f"The content of grade object with vars is {vars(grade)}")
# An error occurs when trying to create a new object from the class after deleting the class
# It is not possible to create a new object from the class after deleting the class




