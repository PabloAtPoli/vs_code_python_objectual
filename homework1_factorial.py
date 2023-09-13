"""
Finds the factorial of a number using procedural and functional programming

"""

def factorial_iterative(n):
    """Returns the factorial of a number iteratively using a for loop"""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    """Returns the factorial of a number recursively"""
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n-1)
    
def main():
    """Tests the factorial functions"""
    print("Factorial of 5 iterative is", factorial_iterative(5))
    print("Factorial of 5 recursive is ",factorial_recursive(5))
    print("Factorial of 59 iterative is", factorial_iterative(59))
    print("Factorial of 59 recursive is ",factorial_recursive(59))
          
    print("Factorial of large numbers")
    print("Factorial of 1000 iterative is", factorial_iterative(1000))
    print("Factorial of 3000 iterative is", factorial_iterative(1000))

    print("Factorial of 1000 recursive is ",factorial_recursive(1000))
    print("Factorial of 3000 recursive is ",factorial_recursive(3000))
    


if __name__ == "__main__":  
    main() 
 


    
