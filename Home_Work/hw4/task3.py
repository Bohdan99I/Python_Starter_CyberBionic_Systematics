height = int(input("Введіть висоту трикутника: "))

for i in range(1, height + 1):
    for j in range(i):
        print('*', end='')  
    print()  
