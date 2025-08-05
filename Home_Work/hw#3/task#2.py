import math

x = float(input("Введіть значення x (від -π до π): "))

if -math.pi <= x <= math.pi:
    y = math.cos(3 * x)
    print("Значення функції y = cos(3x):", y)
else:
    print("Помилка: значення x має бути в межах від -π до π.")