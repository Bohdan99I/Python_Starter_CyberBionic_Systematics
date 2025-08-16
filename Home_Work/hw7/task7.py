staff = {}

def print_employee(lastname, data):
    print(f"\nПрізвище: {lastname}")
    for key, value in data.items():
        print(f"  {key}: {value}")

while True:
    print("\n=== МЕНЮ ОБЛІКУ КАДРІВ ===")
    print("1 - Переглянути всіх співробітників")
    print("2 - Додати або змінити співробітника")
    print("3 - Сортувати за прізвищем")
    print("4 - Показати найефективнішого співробітника")
    print("5 - Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        if staff:
            print("\nСписок співробітників:")
            for lastname, data in staff.items():
                print_employee(lastname, data)
        else:
            print("Дані відсутні.")

    elif choice == "2":
        lastname = input("Введіть прізвище: ").strip()
        if not lastname:
            print("Прізвище не може бути пустим.")
            continue
        posada = input("Посада: ").strip()
        dosvid = input("Досвід роботи: ").strip()
        portfolio = input("Портфоліо: ").strip()
        try:
            efficiency = float(input("Коефіцієнт ефективності (число): ").strip())
        except ValueError:
            print("Некоректне число для коефіцієнта ефективності.")
            continue
        tech_stack = input("Стек технологій (через кому): ").strip()
        try:
            salary = float(input("Зарплата (число): ").strip())
        except ValueError:
            print("Некоректне число для зарплати.")
            continue

        staff[lastname] = {
            "посада": posada,
            "досвід роботи": dosvid,
            "портфоліо": portfolio,
            "коефіцієнт ефективності": efficiency,
            "стек технологій": tech_stack,
            "зарплата": salary
        }
        print("Співробітника додано/оновлено.")

    elif choice == "3":
        if staff:
            print("\nСпівробітники за прізвищем:")
            for lastname, data in sorted(staff.items()):
                print_employee(lastname, data)
        else:
            print("Дані відсутні.")

    elif choice == "4":
        if staff:
            best = max(staff.items(), key=lambda x: x[1].get("коефіцієнт ефективності", 0))
            print("\nНайефективніший співробітник:")
            print_employee(best[0], best[1])
        else:
            print("Дані відсутні.")

    elif choice == "5":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")
