# Знайти різницю між двома списками (десять значень першого та другого значення вести із клавіатури як два списки, роздрукувати всі значення із першого списку які не входять у 2 список і навпаки)

list1 = []
list2 = []

print("10 значень для 1 списку:")
for i in range(10):
    value = input(f"Значення {i + 1}: ")
    list1.append(value)

print("\n10 значень для 2 списку:")
for i in range(10):
    value = input(f"Значення {i + 1}: ")
    list2.append(value)

set1 = set(list1)
set2 = set(list2)

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)

print("\nЗначення з 1 списку, яких немає у 2:", list(diff1))
print("Значення з 2 списку, яких немає у 1:", list(diff2))