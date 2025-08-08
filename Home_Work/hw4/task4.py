a = int(input("Введіть число a (менше за b): "))
b = int(input("Введіть число b (більше за a): "))

if a >= b or a < 1:
    print("Помилка: число a повинно бути меншим за b і обидва мають бути натуральними.")
else:
    avg = (a + b) / 2 
    total = 0

    for i in range(a, b + 1):
        if i % avg == 0:
            total += i

    print(f"Сума чисел від {a} до {b}, які кратні середньому арифметичному ({avg}): {int(total)}")
