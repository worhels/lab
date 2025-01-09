import os
import csv
from lab_02 import load_data, save_data, student_list

# Подготовка тестового файла
TEST_FILE = "test_lab2.csv"

def setup_test_file():
    test_data = [
        {"name": "Alice", "phone": "123456", "email": "alice@example.com", "address": "Wonderland"},
        {"name": "Bob", "phone": "654321", "email": "bob@example.com", "address": "Builderland"}
    ]
    with open(TEST_FILE, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(test_data)
    print(f"Тестовый файл {TEST_FILE} создан.")

# Тест: Загрузка данных
def test_load_data():
    print(f"Список до загрузки: {student_list}")
    load_data(TEST_FILE)
    print(f"Список после загрузки: {student_list}")
    assert len(student_list) > 0, "Данные не загружены."

# Тест: Добавление студента
def test_add_student():
    initial_count = len(student_list)
    student_list.append({"name": "Test Student", "phone": "123456", "email": "test@example.com", "address": "Test Address"})
    assert len(student_list) == initial_count + 1, "Студент не добавлен."

# Тест: Сохранение данных
def test_save_data():
    save_data("test_save.csv")
    assert os.path.exists("test_save.csv"), "Файл не сохранён."
    with open("test_save.csv", "r") as file:
        assert file.read(), "Файл не содержит данных."

if __name__ == "__main__":
    # Подготовка тестового окружения
    setup_test_file()

    # Запуск тестов
    try:
        test_load_data()
        test_add_student()
        test_save_data()
        print("Все тесты успешно пройдены!")
    except AssertionError as e:
        print(f"Ошибка: {e}")
