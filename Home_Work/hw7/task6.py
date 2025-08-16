library = {
    "Шевченко": "Кобзар",
    "Франко": "Захар Беркут",
    "Леся Українка": "Лісова пісня"
}

while True:
    print("\n=== МЕНЮ БІБЛІОТЕКИ ===")
    print("1 - Переглянути всі записи")
    print("2 - Додати новий запис")
    print("3 - Сортувати за автором")
    print("4 - Сортувати за твором")
    print("5 - Вихід")

    choice = input("Оберіть дію: ")

    if choice == "1":
        print("\nВсі записи:")
        for author, work in library.items():
            print(f"{author}: {work}")

    elif choice == "2":
        author = input("Введіть ім'я автора: ")
        work = input("Введіть назву твору: ")
        library[author] = work
        print("Запис додано!")

    elif choice == "3":
        print("\nСортування за автором:")
        for author, work in sorted(library.items()):
            print(f"{author}: {work}")

    elif choice == "4":
        print("\nСортування за твором:")
        for author, work in sorted(library.items(), key=lambda x: x[1]):
            print(f"{author}: {work}")

    elif choice == "5":
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір, спробуйте ще раз.")
