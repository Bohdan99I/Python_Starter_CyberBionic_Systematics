def recursive_sum(start, end):
    if start > end:
        return 0
    return start + recursive_sum(start + 1, end)


try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))

    start, end = min(a, b), max(a, b)

    result = recursive_sum(start, end)
    print(f"Сума чисел від {start} до {end} = {result}")

except ValueError:
    print("Помилка! Введіть цілі числа.")