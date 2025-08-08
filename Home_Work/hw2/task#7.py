length = 700        # Відстань у км
velocity = 90       # Швидкість у км/год

driving_time = length // velocity  # Ціле ділення
remainder = length % velocity      # Залишок кілометрів

print("Час у годинах:", driving_time, "годин")
print("Залишок відстані:", remainder, "км")


# Час у форматі 00 годин 00 хвилин
length = 700       
velocity = 90       

total_hours = length / velocity

hours = int(total_hours)  # Ціла частина — години
minutes = int((total_hours - hours) * 60)  # Залишок * 60 = хвилини

print("Час у дорозі:", str(hours) + " годин " + str(minutes) + " хвилин")