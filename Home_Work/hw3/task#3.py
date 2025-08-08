import math

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

D = b**2 - 4*a*c

if D < 0:
    print("Рівняння не має дійсних коренів.")
elif D == 0:
    x = -b / (2 * a)
    print("Рівняння має один дійсний корінь:", x)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Рівняння має два дійсні корені:")
    print("x1 =", x1)
    print("x2 =", x2)