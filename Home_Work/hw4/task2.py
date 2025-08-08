n = int(input("Введіть ціле невід’ємне число n: "))

if n < 0:
    print("Факторіал визначено лише для невід’ємних чисел.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факторіал {n}! = {factorial}")
5