links = {}

while True:
    print("\nМеню:")
    print("1 - Додати посилання")
    print("2 - Отримати початкове посилання")
    print("3 - Вихід")

    choice = input("Виберіть дію: ")

    if choice == "1":
        original = input("Введіть початкове посилання: ")
        short = input("Введіть коротку назву: ")
        links[short] = original
        print("Посилання збережено!")

    elif choice == "2":
        short = input("Введіть коротку назву: ")
        if short in links:
            print("Початкове посилання:", links[short])
        else:
            print("Такої короткої назви немає у базі.")

    elif choice == "3":
        print("Вихід із програми.")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")
