# Знайти мінімальне, максимальне і середнє значення з 10 чисел 

numbers = []

for i in range(10):
    while True:
        try:           
            num = int(input(f"Введіть число {i+1} з 10: "))          
            numbers.append(num)
            break
        except ValueError:            
            print("Некоректний ввід. Будь ласка, введіть ціле число.")

min_value = min(numbers)
max_value = max(numbers)
average_value = sum(numbers) / len(numbers)


print("\n Результати:")
print(f"Введені числа: {numbers}")
print(f"Мінімальне: {min_value}")
print(f"Максимальне: {max_value}")
print(f"Середнє: {average_value}")

numbers = []

for i in range(10):
    while True:
        try:
            num = int(input(f"Введіть число {i+1} з 10: "))
            numbers.append(num)
            break
        except ValueError:
            print("Некоректний ввід. Будь ласка, введіть ціле число.")

min_value = numbers[0]
max_value = numbers[0]
total_sum = 0
count = 0

for num in numbers:
    if num < min_value:
        min_value = num
        
    if num > max_value:
        max_value = num
  
    total_sum += num
  
    count += 1

average_value = total_sum / count

print("\nРезультати:")
print(f"Введені числа: {numbers}")
print(f"Мінімальне: {min_value}")
print(f"Максимальне: {max_value}")
print(f"Середнє: {average_value}")