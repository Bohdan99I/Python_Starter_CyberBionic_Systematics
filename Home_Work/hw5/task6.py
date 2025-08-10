feedback = input("Залиште, будь ласка, свій фідбек про курорт «Морська зірка»: ").lower()

keywords = ["меню", "спортзал", "обслуговування"]

discount = 0
for word in keywords:
    if word in feedback:
        discount += 5

if len(feedback) > 60:
    discount += 15

print(f"Ваша знижка на наступне відвідування: {discount}%")