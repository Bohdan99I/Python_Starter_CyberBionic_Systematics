list1 = list(map(int, input("Введіть елементи першого списку через пробіл: ").split()))
list2 = list(map(int, input("Введіть елементи другого списку через пробіл: ").split()))

unique_1 = set(list1) - set(list2)
unique_2 = set(list2) - set(list1)

result_set = unique_1.union(unique_2)
result_list = list(result_set)

print("Пряма послідовність:", result_list)
print("Зворотня послідовність:", result_list[::-1])

sorted_asc = sorted(result_list)
print("Сортування за зростанням:", sorted_asc)

sorted_desc = sorted(result_list, reverse=True)
print("Сортування за спаданням:", sorted_desc)
