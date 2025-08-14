# Знайти кількість унікальних товарів

inventory = ["яблука", "молоко", "хліб", "яйця", "сир"]
print(f"Початковий інвентар: {inventory}")
print("-" * 30)

new_items = ["банани", "сіль", "яйця"] 
print(f"Додаємо 3 нові товари: {new_items}")
inventory.extend(new_items)
print(f"Оновлений інвентар після додавання: {inventory}")
print("-" * 30)

item_to_check1 = "хліб"
item_to_check2 = "цукор"

if item_to_check1 in inventory:
    print(f"Перевірка: Товар '{item_to_check1}' є в наявності.")
else:
    print(f"Перевірка: Товар '{item_to_check1}' відсутній.")

if item_to_check2 in inventory:
    print(f"Перевірка: Товар '{item_to_check2}' є в наявності.")
else:
    print(f"Перевірка: Товар '{item_to_check2}' відсутній.")
print("-" * 30)

item_to_remove1 = "молоко"
item_to_remove2 = "цукерки"

if item_to_remove1 in inventory:
    inventory.remove(item_to_remove1)
    print(f"Успішно видалено: '{item_to_remove1}'.")
else:
    print(f"Помилка: Товар '{item_to_remove1}' неможливо видалити, оскільки його немає в інвентарі.")
    
if item_to_remove2 in inventory:
    inventory.remove(item_to_remove2)
    print(f"Успішно видалено: '{item_to_remove2}'.")
else:
    print(f"Помилка: Товар '{item_to_remove2}' неможливо видалити, оскільки його немає в інвентарі.")

print(f"Інвентар після спроб видалення: {inventory}")
print("-" * 30)

unique_items_count = len(set(inventory))

print(f"Інвентар містить: {len(inventory)} товарів.")
print(f"Кількість унікальних товарів: {unique_items_count}")