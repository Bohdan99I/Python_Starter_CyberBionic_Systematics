def average_of_three(a, b, c):
    return (a + b + c) / 3

while True:
    print("\nВведіть три числа для обчислення середнього арифметичного (або 'stop' для завершення)")
    user_input = input("Перше число: ")
    if user_input.lower() == "stop":
        print("Програму завершено.")
        break
    try:
        a = float(user_input)
        b = float(input("Друге число: "))
        c = float(input("Третє число: "))
        avg = average_of_three(a, b, c)
        print(f"Середнє арифметичне: {avg:.2f}")
    except ValueError:
        print("Помилка: введіть коректні числові значення!")
