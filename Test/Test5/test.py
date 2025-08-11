while True:
    try:
        r = int(input("Введіть Red (0-255): "))
        if 0 <= r <= 255:
            break
        else:
            print("Помилка: Red має бути від 0 до 255.")
    except ValueError:
        print("Помилка: введіть дані ще раз.")

while True:
    try:
        g = int(input("Введіть Green (0-255): "))
        if 0 <= g <= 255:
            break
        else:
            print("Помилка: Green має бути від 0 до 255.")
    except ValueError:
        print("Помилка: введіть дані ще раз.")

while True:
    try:
        b = int(input("Введіть Blue (0-255): "))
        if 0 <= b <= 255:
            break
        else:
            print("Помилка: Blue має бути від 0 до 255.")
    except ValueError:
        print("Помилка: введіть дані ще раз.")

color = (r, g, b)
print(f"Кортеж кольору: {color}")