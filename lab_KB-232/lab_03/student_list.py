from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, name: str):
        self.students = [s for s in self.students if s.name != name]

    def update_student(self, name: str, **kwargs):
        for student in self.students:
            if student.name == name:
                student.name = kwargs.get("name", student.name)
                student.phone = kwargs.get("phone", student.phone)
                student.email = kwargs.get("email", student.email)
                student.age = kwargs.get("age", student.age)

    def display_students(self):
        for student in self.students:
            print(student)
