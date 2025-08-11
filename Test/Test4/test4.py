PRICE_PER_BREAD = 30
TOTAL_COST = 0

print("Ласкаво просимо!")
print("Ціна за 1 хлібину: 30 грн.")

while True:
    quantity = int(input("Введіть кількість хлібин (або 0 для завершення): "))

    if quantity == 0:
        print("\nДякуємо за покупку!")
        break
    elif quantity > 0:
        cost = quantity * PRICE_PER_BREAD
        TOTAL_COST += cost
        print(f"Додано до кошика: {quantity} хлібин. Вартість: {cost} грн.")
    else:
        print("Будь ласка, введіть додатне число.")

print(f"Загальна сума до сплати: {TOTAL_COST} грн.")