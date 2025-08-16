str1 = input("Введіть перший рядок: ")
str2 = input("Введіть другий рядок: ")

common_chars = set(str1) & set(str2)

print("Символи, які є в обох рядках:", ''.join(common_chars))
