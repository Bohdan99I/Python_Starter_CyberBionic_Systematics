a = int(input("Введіть (a): "))
b = int(input("Введіть (b): "))

total_sum = 0
count = 0

for number in range(a, b + 1):
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print(f"Сума значень у діапазоні від {a} до {b} дорівнює: {total_sum}")
    print(f"Середнє значення: {average}")
else:
    print("Діапазон порожній.")