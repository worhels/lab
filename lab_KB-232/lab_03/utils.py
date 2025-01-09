import csv
from student import Student
from student_list import StudentList

class Utils:
    @staticmethod
    def load_from_file(filename: str) -> StudentList:
        student_list = StudentList()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = Student(
                        name=row["Name"],
                        phone=row["Phone"],
                        email=row["Email"],
                        age=int(row["Age"])
                    )
                    student_list.add_student(student)
        except FileNotFoundError:
            print(f"Файл {filename} не найден.")
        return student_list

    @staticmethod
    def save_to_file(filename: str, student_list: StudentList):
        with open(filename, "w", encoding="utf-8", newline="") as file:
            fieldnames = ["Name", "Phone", "Email", "Age"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow({
                    "Name": student.name,
                    "Phone": student.phone,
                    "Email": student.email,
                    "Age": student.age
                })
