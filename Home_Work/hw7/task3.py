list1 = [1, 2, 3, 4, 5, 7]
list2 = [4, 5, 6, 7, 8, 9]

unique_list1 = set(list1) - set(list2) 
unique_list2 = set(list2) - set(list1)  

print("Унікальні значення з першого списку:", list(unique_list1))
print("Унікальні значення з другого списку:", list(unique_list2))
