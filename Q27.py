class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course

    def display_student_info(self):
        print(f"Roll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print(f"Course: {self.course}")


class Test(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks  # Dictionary to store subject and marks

    def display_test_info(self):
        self.display_student_info()
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
    

# Example usage
student1 = Test(101, "Alice", "Computer Science", {"Math": 85, "Physics": 90, "Chemistry": 88})
student2 = Test(102, "Bob", "Mechanical Engineering", {"Math": 78, "Mechanics": 88, "Thermodynamics": 92})

print("Student 1 Information:")
student1.display_test_info()

print("\nStudent 2 Information:")
student2.display_test_info()
