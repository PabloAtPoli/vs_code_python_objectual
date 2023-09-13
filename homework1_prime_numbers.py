"""
Generate prime numbers using procedural programming and functional programming

"""

import time


def is_prime_loop(number):
    """Returns True if the number is prime, False otherwise"""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def is_prime_recursive(number, divisor=2):
    """Returns True if the number is prime, False otherwise"""
    if number <= 1:
        return False
    if divisor > int(number ** 0.5):
        return True
    if number % divisor == 0:
        return False
    return is_prime_recursive(number, divisor + 1)

# Timing function


def measure_time(func):
    """Returns the time taken to execute a function"""
    start_time = time.time()
    num = 2
    prime_numbers = []
    while len(prime_numbers) < 1000:
        if func(num):
            prime_numbers.append(num)
        num += 1
    end_time = time.time()
    return prime_numbers, end_time - start_time


# Get the first 1000 prime numbers using loop-based approach
primes_loop, time_loop = measure_time(is_prime_loop)

# Get the first 1000 prime numbers using recursive approach
primes_recursive, time_recursive = measure_time(is_prime_recursive)

# Display results
print("First 1000 prime numbers using loop-based approach:")
print("Length of list primes_loop: ", len(primes_loop), "\n")
print(primes_loop)
print(f"Loop-based approach Running Time: {time_loop:.6f} seconds")

print("\nFirst 1000 prime numbers using recursive approach:")
print("Length of list primes_recursive: ", len(primes_recursive), "\n")
print(primes_recursive)
print(f"Recursive approach Running Time: {time_recursive:.6f} seconds")
