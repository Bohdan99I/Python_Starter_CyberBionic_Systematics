import math


def add(a, b):
    """Додавання двох чисел."""
    return a + b


def subtract(a, b):
    """Віднімання двох чисел."""
    return a - b


def multiply(a, b):
    """Множення двох чисел."""
    return a * b


def divide(a, b):
    """Ділення двох чисел з перевіркою ділення на нуль."""
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b


def power(a, b):
    """Зведення в ступінь."""
    return math.pow(a, b)


def square_root(a):
    """Квадратний корінь."""
    if a < 0:
        return "Помилка: число має бути невід’ємним!"
    return math.sqrt(a)


def cube_root(a):
    """Кубічний корінь."""
    return math.copysign(abs(a) ** (1/3), a)


def sin_value(a):
    """Синус кута (в радіанах)."""
    return math.sin(a)


def cos_value(a):
    """Косинус кута (в радіанах)."""
    return math.cos(a)


def tan_value(a):
    """Тангенс кута (в радіанах)."""
    return math.tan(a)


def calculator():
    """Головне меню інженерного калькулятора."""
    while True:
        print("\n=== Інженерний калькулятор ===")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Зведення в ступінь")
        print("6. Квадратний корінь")
        print("7. Кубічний корінь")
        print("8. Синус (рад)")
        print("9. Косинус (рад)")
        print("10. Тангенс (рад)")
        print("0. Вихід")

        choice = input("Оберіть операцію: ")

        if choice == "0":
            print("Вихід з програми...")
            break

        if choice in ("1", "2", "3", "4", "5"):
            a = float(input("Введіть перше число: "))
            b = float(input("Введіть друге число: "))

            if choice == "1":
                print("Результат:", add(a, b))
            elif choice == "2":
                print("Результат:", subtract(a, b))
            elif choice == "3":
                print("Результат:", multiply(a, b))
            elif choice == "4":
                print("Результат:", divide(a, b))
            elif choice == "5":
                print("Результат:", power(a, b))

        elif choice in ("6", "7", "8", "9", "10"):
            a = float(input("Введіть число (або кут у радіанах): "))

            if choice == "6":
                print("Результат:", square_root(a))
            elif choice == "7":
                print("Результат:", cube_root(a))
            elif choice == "8":
                print("Результат:", sin_value(a))
            elif choice == "9":
                print("Результат:", cos_value(a))
            elif choice == "10":
                print("Результат:", tan_value(a))

        else:
            print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    calculator()