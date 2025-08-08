correct_login = "admin"
correct_password = "1234"

max_attempts = 3

for attempt in range(1, max_attempts + 1):
    login = input("Введіть логін: ")
    password = input("Введіть пароль: ")

    if login == correct_login and password == correct_password:
        print(f"Авторизацію успішно пройдено з {attempt} спроби.")
        break
    else:
        print("Невірний логін або пароль.")
else:
    print("Всі спроби вичерпано. Доступ заборонено.")
