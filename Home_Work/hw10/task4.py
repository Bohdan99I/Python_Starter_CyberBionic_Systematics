def add_item_to_store(store):
    """
    Запитує дані про товар у користувача та додає їх у список на початку.

    :param store: список товарів магазину
    """
    name = input("Введіть назву товару: ")
    price = float(input("Введіть ціну товару: "))
    quantity = int(input("Введіть кількість: "))

    item = (name, price, quantity)

    store.insert(0, item)


def show_store(store):
    """
    Виводить список усіх товарів у магазині.
    """
    if not store:
        print("Магазин порожній.")
        return

    print("\n=== Список товарів у магазині ===")
    for index, (name, price, quantity) in enumerate(store, start=1):
        print(f"{index}. {name} — {price} грн, {quantity} шт.")


def main():
    """
    Головна функція програми.
    """
    store = []

    while True:
        print("\n--- Магазин канцтоварів ---")
        print("1. Додати товар")
        print("2. Показати всі товари")
        print("0. Вихід")

        choice = input("Оберіть дію: ")

        if choice == "1":
            add_item_to_store(store)
        elif choice == "2":
            show_store(store)
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()