"""
A basic calculator module that provides functions for addition, subtraction,
multiplication, and division of two numbers.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Returns the result of subtracting b from a."""
    return a - b


def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b


def divide(a, b):
    """Returns the quotient of a divided by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# --- User Input Section ---
print("Simple Calculator (AI-Generated Docstring Version)")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nResults:")
print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))

try:
    print("Division:", divide(num1, num2))
except ValueError as e:
    print("Error:", e)