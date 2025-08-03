text = input("Введіть фразу з 10 символів: ")

if len(text) != 10:
    print("Помилка: рядок має містити рівно 10 символів.")
else:    
    total = sum(ord(char) for char in text)
    print("Сума ASCII-кодів символів:", total)
