def find_even_numbers_comprehension(numbers):
    """
    Приймає список цілих чисел та повертає список
   
    Args:
        numbers (list): Список цілих чисел.

    Returns:
        list: Список парних чисел.
    """
    return [number for number in numbers if number % 2 == 0]


my_list = [11, 12, 13, 14, 15, 16]
even_list = find_even_numbers_comprehension(my_list)
print(even_list) 


# 2

def f1(x):
    return x**2 + 2 * x + 1


def f2(x):
    import math

    return math.sin(x) + math.cos(x)


print(f"{'x':>6} | {'f1(x)':>10} | {'f2(x)':>10}")
print("-" * 32)

x = -5.0
while x <= 5.0:
    print(f"{x:6.2f} | {f1(x):10.4f} | {f2(x):10.4f}")
    x += 0.5

##### new add-max-function
