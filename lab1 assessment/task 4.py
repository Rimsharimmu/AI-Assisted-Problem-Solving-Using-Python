# Write a Python function to compute factorial using recursion and iteration with user input.
def factorial_recursive(n: int) -> int:
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n: int) -> int:
    """Calculate factorial using iteration."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        n = int(input("Enter a non-negative integer: ").strip())
        if n < 0:
            raise ValueError
    except ValueError:
        print("Invalid input — please enter a non-negative integer.")
    else:
        print(f"{n}! (iterative)  = {factorial_iterative(n)}")
        try:
            print(f"{n}! (recursive)  = {factorial_recursive(n)}")
        except RecursionError:
            print("Recursive computation failed: recursion depth exceeded.")
