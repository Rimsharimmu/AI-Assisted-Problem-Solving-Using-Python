class sru_student:
    """Class to represent SR University student details and fee information."""

    def __init__(self, name, roll_no, hostel_status):
        # Initialize student attributes
        self.name = name                 # Store student's name
        self.roll_no = roll_no           # Store student's roll number
        self.hostel_status = hostel_status  # Indicate whether student stays in hostel (Yes/No)
        self.fee = 0                     # Initialize fee to 0

    def fee_update(self):
        # Update fee based on hostel status
        if self.hostel_status.lower() == "yes":
            self.fee = 80000             # Hostel students pay 80,000
        else:
            self.fee = 60000             # Day scholars pay 60,000

    def display_details(self):
        # Display all student details
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Total Fee:", self.fee)


# --- User Input Section ---
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Is the student staying in hostel? (Yes/No): ")

# Create object and display details
student = sru_student(name, roll_no, hostel_status)
student.fee_update()
student.display_details()