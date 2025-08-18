def f1(x):
       return x**2 + 2*x + 1

def f2(x):
    import math
    return math.sin(x) + math.cos(x)

print(f"{'x':>6} | {'f1(x)':>10} | {'f2(x)':>10}")
print("-" * 32)

x = -5.0
while x <= 5.0:
    print(f"{x:6.2f} | {f1(x):10.4f} | {f2(x):10.4f}")
    x += 0.5
