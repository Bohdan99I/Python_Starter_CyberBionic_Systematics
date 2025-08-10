full_name = input("Введіть ваше ПІБ (Прізвище Ім'я По батькові): ")

words = full_name.split()
capitalized = all(word.istitle() for word in words)
only_letters = all(word.isalpha() for word in words)

if capitalized and only_letters:
    print("Рядок правильний: усі слова з великої літери й містять лише літери.")
else:
    print("Помилка: переконайтесь, що всі слова з великої літери та містять тільки літери.")
