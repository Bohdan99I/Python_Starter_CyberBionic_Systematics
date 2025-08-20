def ways_to_climb(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


while True:
    steps = input("Введіть кількість сходинок (або 'stop' для виходу): ")
    if steps.lower() == "stop":
        print("Програму завершено.")
        break
    if steps.isdigit():
        n = int(steps)
        print(f"Кількість способів піднятися на {n} сходинок: {ways_to_climb(n)}")
    else:
        print("Будь ласка, введіть ціле число.")
