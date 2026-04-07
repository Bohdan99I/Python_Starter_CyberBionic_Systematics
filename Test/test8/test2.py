def analyze_lists(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    unique_values = set1.union(set2)
   
    in_first = set1.difference(set2)
    
    in_second = set2.difference(set1)
    return {
        'unique_values': list(unique_values),
        'in_first': list(in_first),
        'in_second': list(in_second)
    }

list_a = [1, 2, 3, 4, 5, 2]
list_b = [4, 5, 6, 7, 8, 8]

results = analyze_lists(list_a, list_b)

print("Усі унікальні значення:", results['unique_values'])
print("У першому списку, але немає в другому:", results['in_first'])
print("У другому списку, але немає в першому:", results['in_second'])

# 2 варіант
def analyze_lists(list1, list2):
  
    set1 = set(list1)
    set2 = set(list2)

    return {
        'unique_values': list(set1 | set2),
        'in_first': list(set1 - set2),
        'in_second': list(set2 - set1)
    }

list_a = [1, 2, 3, 4, 5, 2]
list_b = [4, 5, 6, 7, 8, 8]

results = analyze_lists(list_a, list_b)

print("Усі унікальні значення:", results['unique_values'])
print("У першому списку, але немає в другому:", results['in_first'])
print("У другому списку, але немає в першому:", results['in_second'])