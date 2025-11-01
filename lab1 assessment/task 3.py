 # Function to reverse a string
# ...existing code...

def reverse_string(s: str) -> str:
    """Return a new string that is the reverse of s."""
    return s[::-1]

# ...existing code...
if __name__ == "__main__":
    print(reverse_string(input("Enter a string: ")))