"""
Factorial using procedural and functional programming


"""
def factorial_procedural(n):
    # Returns the factorial of a number iteratively using a for loop
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Functional Implementation using recursion
def factorial_recursive(n):
    """Returns the factorial of a number recursively"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

# Test with small numbers
numbers_to_test = [3, 4, 5, 10, 15]

print("Factorial using procedural code:")
for num in numbers_to_test:
    print(f"{num}! = {factorial_procedural(num)}")

print("\nFactorial using functional code (recursion):")
for num in numbers_to_test:
    print(f"{num}! = {factorial_recursive(num)}")

# Test with large numbers
print("\nFactorial of large numbers:")
print(f"1000! = {factorial_procedural(1000)}\n")
print(f"3000! = {factorial_procedural(3000)}\n")

print(f"1000! = {factorial_recursive(1000)}\n")
print(f"3000! = {factorial_recursive(3000)}\n")



