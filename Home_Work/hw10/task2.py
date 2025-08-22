import math
import random
from math import pi, e


count = int(input("Введіть кількість повторів: "))

value = 5
print(value * count)
print(pi * value * count)
print(e * 2)

while value >= 0:
    value -= 1

text = "my string"
total = 0

for elem in text:
    total += pow(text.find(elem), 2)
    print("sum =", total)


def my_func(attr=1):
    """Функція для прикладу."""
    print("attr =", attr)


print(my_func(attr=5))
