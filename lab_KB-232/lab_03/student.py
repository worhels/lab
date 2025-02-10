class Student:
    def __init__(self, name: str, phone: str, email: str, age: int):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет, Телефон: {self.phone}, Email: {self.email}"
