
import math


# Define a string variable and assigns the string “Juan Pablo Ortiz Medina”
name = "Juan Pablo Ortiz Medina"

# Print the first letter of the string
print(name[0])

# Print the last letter of the string
print(name[-1])

# Using slicing over the string variable you defined, print in separate lines the substrings “Juan”, “Pablo”, “Ortiz”, and “Medina”
print(name[0:4])
print(name[5:10])
print(name[11:16])
print(name[17:])

# Print the string “ Juan \Pablo\ ‘Ortiz’ “Medina” “
name = "Juan \\Pablo\\ 'Ortiz' \"Medina\""
print(name)

# Define the following variables:
# math_mark = 4.5
# science_mark = 3.5
# Using formatted strings print the string “Math mark = 4.5, science mark = 3.5, my average is 4.0”
# Use an expression in the formatted string to calculate the average
math_mark = 4.5
science_mark = 3.5
print(f"Math mark = {math_mark}, science mark = {science_mark}, my average is {(math_mark+science_mark)/2}")


myString = " juan PABLO ortiz medina"

print(myString.find("BABLO"))

# In one statement (one line of code) print the following string: "JUAN pablo Ortiz Medina"
print(myString.rstrip()[:5].upper() + myString.rstrip()[5:12].lower()+ myString.rstrip()[12:].title())

print(math.ceil(2.2))
print(round(2.2))

# Using the math module, make a program that calculate the factorial of 5
print(f"Factorial of 5 is: {math.factorial(5)}")

# Write a program that reads an integer and float and prints the average of the two numbers. Use formatted string to print the output.
# integer = int(input("Enter an integer: "))
# float_number = float(input("Enter a float number: "))
# print(f"Average of {integer} and {float_number} is {(integer+float_number)/2}")


fruit = "apple"
print(fruit[1:-1])

