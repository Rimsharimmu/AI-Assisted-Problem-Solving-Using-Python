"""
calculator_module.py

A simple calculator module that performs basic arithmetic operations.
This module demonstrates the use of NumPy-style docstrings for multiple functions.
"""

def add(a, b):
    """
    Add two numbers.

    Parameters
    ----------
    a : float
        First number to add.
    b : float
        Second number to add.

    Returns
    -------
    float
        Sum of a and b.

    Example
    -------
    >>> add(5, 3)
    8
    """
    return a + b


def subtract(a, b):
    """
    Subtract two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number to subtract from the first.

    Returns
    -------
    float
        Result of a - b.

    Example
    -------
    >>> subtract(10, 4)
    6
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : float
        First number.
    b : float
        Second number.

    Returns
    -------
    float
        Product of a and b.

    Example
    -------
    >>> multiply(2, 5)
    10
    """
    return a * b


def divide(a, b):
    """
    Divide two numbers.

    Parameters
    ----------
    a : float
        Numerator.
    b : float
        Denominator.

    Returns
    -------
    float
        Result of division (a / b).

    Raises
    ------
    ValueError
        If b is zero.

    Example
    -------
    >>> divide(10, 2)
    5
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


# --- User Input Section ---
print("Simple Calculator")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))
print("Multiplication:", multiply(num1, num2))
print("Division:", divide(num1, num2))