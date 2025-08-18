import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Помилка: неможливо обчислити корінь з від’ємного числа!"
    return math.sqrt(a)

def cbrt(a):
        return a ** (1/3)

while True:
    print("\nДоступні операції:")
    print("1 — Додавання")
    print("2 — Віднімання")
    print("3 — Множення")
    print("4 — Ділення")
    print("5 — Зведення в ступінь")
    print("6 — Квадратний корінь")
    print("7 — Кубічний корінь")
    print("0 — Вихід")
    
    choice = input("Оберіть операцію: ")
    
    if choice == "0":
        print("Програма завершена.")
        break
    
    if choice in ["1", "2", "3", "4", "5"]:
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
    
    elif choice in ["6", "7"]:
        a = float(input("Введіть число: "))
        
        if choice == "6":
            print("Результат:", sqrt(a))
        elif choice == "7":
            print("Результат:", cbrt(a))
    
    else:
        print("Невірний вибір! Спробуйте ще раз.")
