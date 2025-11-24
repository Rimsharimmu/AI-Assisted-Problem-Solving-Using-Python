# ...existing code...
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    while True:
        s = input("Enter a positive integer: ").strip()
        if not s:
            print("Input cannot be empty. Try again.")
            continue
        try:
            num = int(s)
            if num <= 0:
                print("Please enter a positive integer greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid positive integer.")

    seq = fibonacci(num)
    print(f"Fibonacci sequence of {num} term{'s' if num != 1 else ''}:")
    print(seq)

if __name__ == "__main__":
    main()
# ...existing code...