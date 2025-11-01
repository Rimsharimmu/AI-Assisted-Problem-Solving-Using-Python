def check_palindrome():
    """
    Get user input and check if it's a palindrome while ignoring case and spaces.
    Returns True if palindrome, False otherwise.
    """
    # Get user input and clean it
    text = input("Enter text to check if it's a palindrome: ").strip()
    # Handle empty input
    if not text:
        print("No input provided!")
        return False
    
    # Remove spaces and convert to lowercase
    cleaned = ''.join(text.lower().split())
    
    # Compare string with its reverse
    is_palindrome = cleaned == cleaned[::-1]
    # Print result
    if is_palindrome:
        print(f'"{text}" is a palindrome!')
    else:
        print(f'"{text}" is not a palindrome.')
    
    return is_palindrome

if __name__ == "__main__":
    while True:
        check_palindrome()