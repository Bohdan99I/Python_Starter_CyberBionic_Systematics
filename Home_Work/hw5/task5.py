numbers_input = input("Введіть послідовність чисел через пробіл: ")

numbers_list = list(map(int, numbers_input.split()))
numbers_tuple = tuple(numbers_list)
sorted_tuple = tuple(sorted(numbers_tuple))

print("Відсортований кортеж:", sorted_tuple)