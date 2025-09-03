"""
Демонстрація роботи деяких вбудованих функцій Python:
- abs()     : модуль числа
- round()   : округлення числа
- min(), max(), sum(), len(), sorted() : робота з послідовностями
- type()    : визначення типу
- pow(), divmod() : обчислення степеня і ділення з остачею
- all(), any()    : булеві функції для ітерованих об'єктів
"""

# abs() – модуль числа
print("abs(-7) =", abs(-7))

# round() – округлення
print("round(3.14159, 2) =", round(3.14159, 2))

# min(), max(), sum(), len(), sorted()
numbers = [4, 1, 7, 2, 9]
print("min(numbers) =", min(numbers))
print("max(numbers) =", max(numbers))
print("sum(numbers) =", sum(numbers))
print("len(numbers) =", len(numbers))
print("sorted(numbers) =", sorted(numbers))

# type()
print("type(3.14) =", type(3.14))

# pow(), divmod()
print("pow(2, 5) =", pow(2, 5))
print("divmod(17, 5) =", divmod(17, 5))

# all(), any()
bool_list = [True, True, False]
print("all(bool_list) =", all(bool_list))
print("any(bool_list) =", any(bool_list))
