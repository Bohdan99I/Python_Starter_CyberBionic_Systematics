# Рекурсивна функція для обчислення суми чисел у діапазоні
def recursive_sum_range(start, end):

    if start > end:
        start, end = end, start

    if start == end:
        return start
    else:
        return start + recursive_sum_range(start + 1, end)


try:
    num1 = int(input("Введіть перше число: "))
    num2 = int(input("Введіть друге число: "))

    total_sum = recursive_sum_range(num1, num2)
    print(f"Сума чисел у діапазоні від {min(num1, num2)} до {max(num1, num2)} (включно) = {total_sum}")

except ValueError:
    print("Будь ласка, введіть цілі числа.")