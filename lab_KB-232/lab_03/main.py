from utils import Utils
from student import Student

def main():
   
    student_list = Utils.load_from_file("students.csv")
    print("\nТекущий список студентов:")
    student_list.display_students()

   
    print("\nДобавляем нового студента...")
    student_list.add_student(Student("Иван Иванов", "123-456", "ivan@example.com", 20))
    print("\nСписок студентов после добавления:")
    student_list.display_students()

   
    print("\nОбновляем данные студента...")
    student_list.update_student("Иван Иванов", phone="789-012", email="ivan_ivanov@example.com")
    print("\nСписок студентов после обновления:")
    student_list.display_students()

   
    print("\nУдаляем студента...")
    student_list.remove_student("Иван Иванов")
    print("\nСписок студентов после удаления:")
    student_list.display_students()

   
    print("\nСохраняем изменения...")
    Utils.save_to_file("students.csv", student_list)
    print("\nДанные сохранены. Конечный список студентов:")
    student_list.display_students()

if __name__ == "__main__":
    main()
