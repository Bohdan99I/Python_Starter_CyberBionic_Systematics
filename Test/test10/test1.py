def recursive_sum(start_num, end_num):
    if start_num > end_num:
        return 0
    return start_num + recursive_sum(start_num + 1, end_num)


try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))

    start, end = min(a, b), max(a, b)

    result = recursive_sum(start, end)
    print(f"Сума чисел від {start} до {end} = {result}")

except ValueError:
    print("Помилка! Введіть цілі числа.")
    