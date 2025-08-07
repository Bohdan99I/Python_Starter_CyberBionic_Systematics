import math

while True:
    print("\nОберіть операцію:")
    print("1. Розрахунок площі та периметру паралелепіпеда")
    print("2. Розрахунок об'єму кулі")
    print("3. Вийти з програми")

    choice = input("Ваш вибір (1, 2 або 3): ")

    if choice == '1':
        try:
            a = float(input("Введіть довжину: "))
            b = float(input("Введіть ширину: "))
            c = float(input("Введіть висоту: "))            
       
            para_area = 2 * (a * b + a * c + b * c)        
        
            para_perimeter = 4 * (a + b + c)

            print(f"Площа поверхні паралелепіпеда: {para_area}")
            print(f"Периметр паралелепіпеда: {para_perimeter}")
        except ValueError:
            print("Неправильне введення. Будь ласка, введіть числові значення.")

    elif choice == '2':
        try:
            r = float(input("Введіть радіус кулі: "))
            
            spher = (4/3) * math.pi * r**3
            
            print(f"Об'єм кулі: {spher}")
        except ValueError:
            print("Неправильне введення. Будь ласка, введіть числове значення.")

    elif choice == '3':
        print("Завершення програми.")
        break  

    else:
        print("Неправильний вибір. Будь ласка, оберіть 1, 2 або 3.")