# 📌 Шпаргалка по PEP 8 (Python Style Guide)

| Правило        | Приклад ✅                                  | Приклад ❌                             |
| -------------- | ------------------------------------------- | -------------------------------------- |
| Відступи       | `def func():\n    return 42`                | `def func():\n\treturn 42`             |
| Довжина рядка  | `x = "це довгий рядок..."` (до 79 символів) | Рядок у 150 символів                   |
| Порожні рядки  | 2 порожні рядки між функціями/класами       | Без відступів                          |
| Імпорти        | `import os`<br>`import sys`                 | `import os, sys`                       |
| Іменування     | `my_variable`, `UserProfile`, `MAX_SIZE`    | `MyVariable`, `userprofile`, `maxSize` |
| Пробіли        | `x = a + b * c`                             | `x=a+b*c`                              |
| Колекції       | `my_list = [1, 2, 3]`                       | `my_list=[1 ,2 ,3 ]`                   |
| Документація   | `"""Опис функції"""`                        | Відсутня документація                  |
| Перенос рядків | `(a + b + c - d)`                           | `a + b + c - d \`                      |

---

## 📖 Приклад коду у стилі PEP 8

```python
import math


MAX_COUNT = 100


class Circle:
    """Клас для роботи з колом."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Обчислює площу кола."""
        return math.pi * self.radius ** 2


def greet(name):
    """
    Повертає вітання для користувача.

    :param name: Ім’я користувача
    :return: Рядок з привітанням
    """
    return f"Привіт, {name}!"
```
