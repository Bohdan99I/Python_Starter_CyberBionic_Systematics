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
