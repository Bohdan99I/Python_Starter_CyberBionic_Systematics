numbers_input = input("Введіть щонайменше 5 чисел через пробіл: ")

numbers = list(map(int, numbers_input.split()))

if len(numbers) < 5:
    print("Помилка: потрібно ввести щонайменше 5 чисел.")
else:
    second = numbers[1]            
    second_last = numbers[-2]         
    average = sum(numbers) / len(numbers) 

    result = second + second_last + average

    print(f"Друге число: {second}")
    print(f"Передостаннє число: {second_last}")
    print(f"Середнє арифметичне: {average}")
    print(f"Сума другого, передостаннього і середнього арифметичного: {result}")
