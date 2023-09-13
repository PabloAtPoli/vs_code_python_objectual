"""
Implement the Fibonacci sequence using both procedural and functional programming.

"""
import time

# Procedural Implementation


def fibonacci_procedural(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])
    return fib_sequence

# Functional Implementation using generator


def fibonacci_functional(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Timing function


def measure_time(func, n):
    start_time = time.time()
    result = list(func(n))
    end_time = time.time()
    return result, end_time - start_time


# Get input from the user
n = int(input("Enter the value of n: "))

# Measure and display the running times
procedural_result, procedural_time = measure_time(fibonacci_procedural, n)
functional_result, functional_time = measure_time(fibonacci_functional, n)

print("Procedural Fibonacci Sequence:")
print(procedural_result)
print(f"Procedural Running Time: {procedural_time:.6f} seconds")

print("\nFunctional Fibonacci Sequence:")
print(functional_result)
print(f"Functional Running Time: {functional_time:.6f} seconds")
