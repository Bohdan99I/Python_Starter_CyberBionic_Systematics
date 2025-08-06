import math

print("Оберіть операцію:")
print("1 - Додавання (+)")
print("2 - Віднімання (-)")
print("3 - Множення (*)")
print("4 - Ділення (/)")
print("5 - Зведення в ступінь (x^y)")
print("6 - Квадратний корінь (√x)")
print("7 - Кубічний корінь (∛x)")
print("8 - Синус (sin x)")
print("9 - Косинус (cos x)")
print("10 - Тангенс (tan x)")

choice = input("Введіть номер операції (1-10): ")

if choice in ['1', '2', '3', '4', '5']:
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))

    if choice == '1':
        result = x + y
        print("Результат:", result)
    elif choice == '2':
        result = x - y
        print("Результат:", result)
    elif choice == '3':
        result = x * y
        print("Результат:", result)
    elif choice == '4':
        if y == 0:
            print("Помилка: ділення на нуль!")
        else:
            result = x / y
            print("Результат:", result)
    elif choice == '5':
        result = x ** y
        print("Результат:", result)

elif choice in ['6', '7', '8', '9', '10']:
    x = float(input("Введіть число: "))

    if choice == '6':
        if x < 0:
            print("Помилка: неможливо обчислити квадратний корінь з від'ємного числа (у дійсних числах).")
        else:
            print("Результат:", x ** 0.5)
    elif choice == '7':
        print("Результат:", x ** (1/3))
    elif choice == '8':
        print("Результат:", math.sin(x))
    elif choice == '9':
        print("Результат:", math.cos(x))
    elif choice == '10':
        print("Результат:", math.tan(x))
else:
    print("Невірний вибір операції.")