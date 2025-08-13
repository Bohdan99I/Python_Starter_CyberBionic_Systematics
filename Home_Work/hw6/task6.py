new_list = [1, 3, 5, 3, 1, 5, 3, 5]  

value = int(input("Введіть значення для пошуку у списку: "))

if value in new_list:
    count = new_list.count(value)
    first_pos = new_list.index(value) 
    print(f"Значення {value} зустрічається {count} раз(ів).")
    print(f"Позиція першої появи у списку: {first_pos}")
else:
    print(f"Значення {value} у списку не знайдено.")
