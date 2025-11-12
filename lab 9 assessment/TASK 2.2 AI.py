class sru_student:
    """Class representing an SRU student with hostel status and fee update functionality."""

    def __init__(self, name, roll_no, hostel_status):
        # Initialize the student object with name, roll number, and hostel status
        self.name = name
        self.roll_no = roll_no
        self.hostel_status = hostel_status
        self.fee = 0  # Initialize fee attribute to 0

    def fee_update(self):
        # Check if student is a hostel resident and update fee accordingly
        if self.hostel_status.lower() == "yes":
            self.fee = 80000  # Set fee to 80000 for hostel students
        else:
            self.fee = 60000  # Set fee to 60000 for non-hostel students

    def display_details(self):
        # Print student details and total fee
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Hostel Status:", self.hostel_status)
        print("Total Fee:", self.fee)


# Take input from user for student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
hostel_status = input("Is the student staying in hostel? (Yes/No): ")

# Create a student object and display fee details
student = sru_student(name, roll_no, hostel_status)
student.fee_update()
student.display_details()