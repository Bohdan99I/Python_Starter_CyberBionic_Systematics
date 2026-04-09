def create_user(name, employee_id, position, salary, is_manager):
    """
    Створюємо користувача.

    Параметри.
       
    Повертаємо:
        dict: Словник, що представляє користувача.
    """
    return {
        "name": name,
        "employee_id": employee_id,
        "position": position,
        "salary": salary,
        "is_manager": is_manager,
    }

users = []

users.append(create_user("Олександр Коваль", "E001", "Менеджер проєкту", 75000, True))
users.append(create_user("Марія Іванова", "E002", "Програміст", 80000, False))
users.append(create_user("Ігор Петренко", "E003", "Аналітик даних", 70000, False))
users.append(create_user("Наталія Семененко", "E004", "HR-менеджер", 55000, True))
users.append(create_user("Віктор Мельник", "E005", "Дизайнер", 60000, False))
users.append(create_user("Олена Ткаченко", "E006", "Маркетолог", 58000, False))
users.append(create_user("Юрій Клименко", "E007", "Бухгалтер", 65000, True))

print("Список користувачів:")
for i, user in enumerate(users):
    print(f"{i}: {user['name']}")
print("-" * 30)

try:
    user_index_str = input("Введіть індекс користувача: ")
    user_index = int(user_index_str)

    if 0 <= user_index < len(users):
        user = users[user_index]
        print("\n--- Інформація про обраного користувача ---")
        print(f"Ім'я: {user['name']}")
        print(f"ID працівника: {user['employee_id']}")
        print(f"Посада: {user['position']}")
        print(f"Зарплата: {user['salary']} грн")
        print(f"Менеджер: {'Так' if user['is_manager'] else 'Ні'}")
        print("-" * 30)
    else:
        print(f"Помилка: Користувача з індексом {user_index} не існує.")

except ValueError:
    print("Помилка: Будь ласка, введіть коректний індекс користувача.")
