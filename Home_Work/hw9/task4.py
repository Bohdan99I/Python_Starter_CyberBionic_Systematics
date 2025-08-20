def sum_range(a, b):
    if a > b:
        return 0   
    if a == b:
        return a   
    return a + sum_range(a + 1, b)


while True:
    data = input("Введіть два числа через пробіл (або 'stop' для виходу): ")
    if data.lower() == "stop":
        print("Програму завершено.")
        break

    try:
        a, b = map(int, data.split())
        result = sum_range(a, b)
        print(f"Сума натуральних чисел від {a} до {b}: {result}")
    except ValueError:
        print("Помилка! Введіть два цілих числа.")
