students = {
    101: {'Roll Number': 1, 'Name': 'Abhi', 'Marks': 85},
    102: {'Roll Number': 2, 'Name': 'omkar', 'Marks': 78},
    103: {'Roll Number': 3, 'Name': 'Charlie', 'Marks': 92}
}

def display_student_info(admno):
    student = students.get(admno)
    if student:
        print(f"Admission Number: {admno}")
        print(f"Roll Number: {student['Roll Number']}")
        print(f"Name: {student['Name']}")
        print(f"Marks: {student['Marks']}")
    else:
        print("Student not found!")

adm_no = int(input("Enter Admission Number to search: "))
display_student_info(adm_no)
