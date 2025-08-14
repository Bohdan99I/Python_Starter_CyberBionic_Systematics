# Знайти кількість унікальних товарів
inventory = ["яблука", "молоко", "хліб", "яйця", "сир"]

inventory.extend(["банани", "сіль", "яйця"])
print(f"Інвентар після додавання: {inventory}")

remove_item = "молоко"
if remove_item in inventory:
    inventory.remove(remove_item)
    print(f"Товар '{remove_item}' видалено.")
else:
    print(f"Товар '{remove_item}' відсутній.")

nonexistent_item = "цукерки"
if nonexistent_item in inventory:
    inventory.remove(nonexistent_item)
    print(f"Товар '{nonexistent_item}' видалено.")
else:
    print(f"Товар '{nonexistent_item}' неможливо видалити, його немає в інвентарі.")
    
print(f"Фінальний інвентар: {inventory}")

unique_items = len(set(inventory))
print(f"Кількість унікальних товарів: {unique_items}")