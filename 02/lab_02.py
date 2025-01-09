import csv
import os
from sys import argv

# Глобальный список студентов
student_list = []

# Загрузка данных из CSV
def load_data(file_name="lab2.csv"):
    global student_list
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            student_list = list(reader)
            print(f"Данные загружены из файла {file_name}.")
    except FileNotFoundError:
        print(f"Файл {file_name} не найден. Будет использован пустой справочник.")

# Сохранение данных в CSV
def save_data(file_name="lab2.csv"):
    global student_list
    with open(file_name, "w", newline='', encoding="utf-8") as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(student_list)
    print(f"Данные сохранены в файл {file_name}.")

# Печать списка студентов
def print_all_students():
    if not student_list:
        print("Список студентов пуст.")
    else:
        for student in student_list:
            print(f"Name: {student['name']}, Phone: {student['phone']}, Email: {student['email']}, Address: {student['address']}")

# Добавление нового студента
def add_student():
    name = input("Введите имя студента: ")
    phone = input("Введите номер телефона: ")
    email = input("Введите email: ")
    address = input("Введите адрес: ")
    new_student = {"name": name, "phone": phone, "email": email, "address": address}

    # Сортируем при добавлении
    insert_position = 0
    for student in student_list:
        if name > student["name"]:
            insert_position += 1
        else:
            break
    student_list.insert(insert_position, new_student)
    print("Студент добавлен в справочник.")

# Удаление студента
def delete_student():
    name = input("Введите имя студента для удаления: ")
    for student in student_list:
        if student["name"] == name:
            student_list.remove(student)
            print(f"Студент {name} удалён из справочника.")
            return
    print(f"Студент с именем {name} не найден.")

# Обновление данных студента
def update_student():
    name = input("Введите имя студента для обновления: ")
    for student in student_list:
        if student["name"] == name:
            print("Обновите информацию. Нажмите Enter, чтобы оставить поле без изменений.")
            new_phone = input(f"Текущий номер телефона ({student['phone']}): ")
            new_email = input(f"Текущий email ({student['email']}): ")
            new_address = input(f"Текущий адрес ({student['address']}): ")

            student["phone"] = new_phone if new_phone else student["phone"]
            student["email"] = new_email if new_email else student["email"]
            student["address"] = new_address if new_address else student["address"]
            print(f"Информация о студенте {name} обновлена.")
            return
    print(f"Студент с именем {name} не найден.")

# Главное меню
def main():
    file_name = "lab2.csv"
    if len(argv) > 1:
        file_name = argv[1]
    
    # Убедимся, что файл находится в текущей папке
    file_path = os.path.join(os.getcwd(), file_name)
    load_data(file_path)

    while True:
        print("\nМеню:")
        print("1. Показать всех студентов")
        print("2. Добавить нового студента")
        print("3. Удалить студента")
        print("4. Обновить данные студента")
        print("5. Сохранить и выйти")
        
        choice = input("Выберите действие (1-5): ")
        if choice == "1":
            print_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            save_data(file_path)
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
