# Знайти суму кожного 7-го значення в діапазоні від X до Y
try:
    start = int(input("Введіть початкове число діапазону: "))
    end = int(input("Введіть кінцеве число діапазону: "))
except ValueError:
    print("Помилка.")
    exit()

total_sum = 0
found_values = []

for number in range(start, end + 1, 7):
    total_sum += number
    found_values.append(number)

print("-" * 25)
print(f"Послідовність чисел: {found_values}")
print(f"Сума кожного 7-го значення в діапазоні від {start} до {end} дорівнює: {total_sum}")