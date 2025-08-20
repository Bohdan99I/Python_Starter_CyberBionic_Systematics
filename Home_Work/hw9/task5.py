import math


def quadratic_equation(a, b, c):    
    x1, x2 = None, None  

    def calc_result(a, b, c):
        nonlocal x1, x2
        D = b**2 - 4*a*c
        print(f"Дискримінант: {D}")

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)
        elif D == 0:
            x1 = x2 = -b / (2 * a)
        else:
            print("Дійсних коренів немає.")
        
    calc_result(a, b, c)
    return [x1, x2]


print("Розв'язання квадратного рівняння ax² + bx + c = 0")

try:
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))

    if a == 0:
        print("Це не квадратне рівняння (a не може бути 0).")
    else:
        roots = quadratic_equation(a, b, c)
        print("Корені рівняння:", roots)

except ValueError:
    print("Помилка! Введіть числа.")
