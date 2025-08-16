from collections import OrderedDict, defaultdict, ChainMap

# 1. OrderedDict 
ordered = OrderedDict()
ordered['apple'] = 3
ordered['banana'] = 5
ordered['cherry'] = 2
print("OrderedDict початковий:", ordered)

ordered.move_to_end('apple')
print("OrderedDict після move_to_end:", ordered)

print("-" * 50)

# 2. defaultdict
dd = defaultdict(int) 
dd['milk'] += 2
dd['bread'] += 1
print("defaultdict:", dd)
print("Отримання неіснуючого ключа 'eggs':", dd['eggs']) 

print("-" * 50)

# 3. ChainMap — об'єднання словників
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 10, 'c': 3}
dict3 = {'d': 4}

cm = ChainMap(dict1, dict2, dict3)
print("ChainMap пошук 'a':", cm['a'])  
print("ChainMap пошук 'b':", cm['b']) 
print("ChainMap пошук 'c':", cm['c']) 
print("ChainMap пошук 'd':", cm['d'])  
