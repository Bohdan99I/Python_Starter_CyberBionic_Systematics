def check_bmi(height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return f"Ваш ІМТ = {bmi:.2f}. Недостатня вага."
    elif 18.5 <= bmi < 25:
        return f"Ваш ІМТ = {bmi:.2f}. Маса тіла в нормі."
    else:
        return f"Ваш ІМТ = {bmi:.2f}. Слідкуйте за фігурою."

while True:
    print("\nВведіть зріст (у метрах) та вагу (у кг), або введіть 'off' для завершення.")
    height_input = input("Зріст (м): ")
    if height_input.lower() == "off":
        print("Програму завершено.")
        break
    
    weight_input = input("Вага (кг): ")
    if weight_input.lower() == "off":
        print("Програму завершено.")
        break
    
    try:
        height = float(height_input)
        weight = float(weight_input)
        if height <= 0 or weight <= 0:
            print("Помилка: зріст і вага повинні бути додатними числами!")
            continue
        print(check_bmi(height, weight))
    except ValueError:
        print("Помилка: введіть коректні числові значення!")
