"""
Use a random variable to implement function that does not fit the functional paradigm
"""

import random
def random_function(n):
    """Returns a random number between 1 and n"""
    return random.randint(1, n)


def main():
    """Tests the random_function"""
    print("Random number between 1 and 50 is", random_function(50))
    print("Random number between 1 and 50 is", random_function(50))

if __name__ == "__main__":
    main()
