n = int(input("Введіть кількість елементів списку: "))
numbers = []

for i in range(n):
    val = int(input(f"Введіть елемент {i+1}: "))
    numbers.append(val)

print("\nМеню:")
print("1 - Вивести список у зворотному порядку")
print("2 - Вивести список за зростанням")

choice = input("Введіть номер операції (1 або 2): ").strip()

if choice == '1':
    print("Список у зворотному порядку:", numbers[::-1])
elif choice == '2':
    print("Список за зростанням:", sorted(numbers))
else:
    print("Невірний вибір.")
