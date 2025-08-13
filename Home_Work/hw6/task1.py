input_list = input("Введіть числа через пробіл: ")

numbers = list(map(int, input_list.split()))

max_num = max(numbers)
min_num = min(numbers)

total = sum(numbers)
average = total / len(numbers)

print(f"Найбільший елемент: {max_num}")
print(f"Найменший елемент: {min_num}")
print(f"Сума елементів: {total}")
print(f"Середнє арифметичне: {average}")
