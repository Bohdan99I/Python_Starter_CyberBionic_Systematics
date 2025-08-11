TOTAL_COST = 0

print("Ласкаво просимо до симулятора касового апарату!")

while True:
    quantity = int(input("Введіть кількість товару (або 0 для завершення): "))

    if quantity == 0:
        print("\nДякуємо за покупку!")
        break
    elif quantity > 0:
        price = float(input("Введіть вартість 1 товару: "))
        cost = quantity * price
        TOTAL_COST += cost
        print(f"Додано до кошика: {quantity} товару. Вартість: {cost} грн.")
    else:
        print("Будь ласка, введіть додатне число.")

print(f"Загальна сума до сплати: {TOTAL_COST} грн.")