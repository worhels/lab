import unittest
from student import Student

class TestStudent(unittest.TestCase):
    def test_create_student(self):
        student = Student("Иван Иванов", "123-456", "ivan@example.com", 20)
        self.assertEqual(student.name, "Иван Иванов")
        self.assertEqual(student.phone, "123-456")
        self.assertEqual(student.email, "ivan@example.com")
        self.assertEqual(student.age, 20)

if __name__ == "__main__":
    unittest.main()
