# new_list = [1, 3, 5, 3, 1, 5, 3, 5]  # приклад для тесту

int_list = list(map(int, input("Введіть натуральні числа через пробіл: ").split()))

new_list = [x for x in int_list if x % 2 != 0]
repeat = int(input("Введіть кількість повторів списку: "))
new_list = new_list * repeat

int_list.clear()

print("Список new_list після дублювання:", new_list)
print("Список int_list після очищення:", int_list)