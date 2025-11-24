class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return "Queue is empty!"
        return self.items.pop(0)

    def peek(self):
        if not self.items:
            return "Queue is empty!"
        return self.items[0]


# ---------- USER INPUT MENU ----------
q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item to add: ")
        q.enqueue(item)
        print("Enqueued:", item)

    elif choice == "2":
        print("Dequeued:", q.dequeue())

    elif choice == "3":
        print("Front element:", q.peek())

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice !")
