"""
It finds the n Fibonacci numbers using functional programming

"""


def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci_recursive(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence


# Get input from the user
n = int(input("Enter the value of n: "))

# Generate the Fibonacci sequence recursively
fib_sequence = fibonacci_recursive(n)

# Display the generated sequence
print("Fibonacci Sequence:")
print(fib_sequence)
