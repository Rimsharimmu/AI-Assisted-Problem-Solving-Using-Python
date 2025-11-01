def calculate_odd_even_sums():
    """
    Calculate separate sums for odd and even numbers from user input.
    Returns tuple of (odd_sum, even_sum).
    """
    try:
        # Get input from user
        numbers = input("Enter numbers separated by spaces: ").strip().split()
        numbers = [int(num) for num in numbers]
        
        # Calculate sums using list comprehension
        even_sum = sum(num for num in numbers if num % 2 == 0)
        odd_sum = sum(num for num in numbers if num % 2 != 0)
        
        # Print results
        print("\nResults:")
        print(f"Even numbers sum: {even_sum}")
        print(f"Odd numbers sum: {odd_sum}")
        
        return (odd_sum, even_sum)
        
    except ValueError:
        print("Error: Please enter valid integers separated by spaces")
        return None

if __name__ == "__main__":
    while True:
        calculate_odd_even_sums()
        
        # Ask if user wants to continue
        again = input("\nCalculate another set of sums? (y/n): ").lower().strip()
        if again != 'y':
            break