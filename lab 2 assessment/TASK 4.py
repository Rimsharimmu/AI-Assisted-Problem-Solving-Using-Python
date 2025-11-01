def sum_of_squares():
    """
    Calculate the sum of squares for a list of numbers provided by user input.
    Returns the sum of squares and prints the calculation details.
    """
    try:
        # Get input from user
        numbers = input("Enter numbers separated by spaces: ").strip().split()
        
        # Convert strings to numbers and calculate squares
        numbers = [float(num) for num in numbers]
        squares = [num * num for num in numbers]
        
        # Calculate sum of squares
        total = sum(squares)
        
        # Print detailed output
        print("\nCalculations:")
        for i, num in enumerate(numbers):
            print(f"{num}² = {squares[i]}")
        print(f"\nSum of squares = {total}")
        
        return total
        
    except ValueError:
        print("Error: Please enter valid numbers separated by spaces")
        return None

if __name__ == "__main__":
    while True:
        sum_of_squares()
        
        # Ask if user wants to continue
        again = input("\nCalculate another sum of squares? (y/n): ").lower().strip()
        if again != 'y':
            break
            
    print("Thank you for using the sum of squares calculator!")