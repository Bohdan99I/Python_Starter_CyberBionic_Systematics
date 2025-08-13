def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Введіть початок проміжку: "))
end = int(input("Введіть кінець проміжку: "))

primes = [num for num in range(start, end + 1) if is_prime(num)]

if primes:
    print("Прості числа в проміжку:", primes)
else:
    print("Простих чисел у цьому проміжку немає.")

choice = input("Введіть 'суму' для обчислення суми простих чисел або 'добуток' для обчислення їх добутку: ").strip().lower()

if choice == "суму":
    print("Сума простих чисел:", sum(primes))
elif choice == "добуток":
    product = 1
    for p in primes:
        product *= p
    print("Добуток простих чисел:", product)
else:
    print("Невірний вибір.")
