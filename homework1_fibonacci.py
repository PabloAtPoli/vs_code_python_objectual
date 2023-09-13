"""
It finds the n numbers of the Fibonacci sequence using procedural and functional programming

"""
import time
def fibonacci_procedural(n):
    """Returns the n numbers of the Fibonacci sequence using a for loop"""
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        fib1 = 0
        fib2 = 1
        for _ in range(2, n):
            fib = fib1 + fib2
            fib_sequence.append(fib)
            fib1 = fib2
            fib2 = fib
        return fib_sequence

def fibonacci_recursive(n):
    """Returns the nth Fibonacci number recursively"""
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

def measure_time(func, n):
    """Measures the running time of a function"""
    start_time = time.time()
    result = list(func(n))
    end_time = time.time()
    return result, end_time - start_time
     
def main():
    """Tests the fibonacci functions"""

    
    # Measure and display the running times
    procedural_result, procedural_time = measure_time(fibonacci_procedural, 500)
    recursive_result, recursive_time = measure_time(fibonacci_recursive, 500)
    
    print("Procedural Fibonacci Sequence:")
    print(procedural_result)
    print(f"Procedural Running Time: {procedural_time} seconds")
    
    print("\nRecursive Fibonacci Sequence:")
    print(recursive_result)
    print(f"Recursive Running Time: {recursive_time} seconds")


if __name__ == "__main__":
    main()
