import string

def find_most_frequent_word(text):
    
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

 
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    if not word_counts:
        return None  

    most_frequent_word = max(word_counts, key=word_counts.get)
    
    return most_frequent_word


test_string = "Привіт, привіт, світ, привіт! Це тестовий рядок для тестування. Тестування, тестування."
most_common = find_most_frequent_word(test_string)

print(f"Слово, що найчастіше зустрічається: '{most_common}'")

# 2 variant

from collections import Counter
import string

def find_most_word(text):

    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    if not words:
        return None  
    
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)

    return most_common[0][0]

test_string = "Привіт, привіт, світ, привіт! Це тестовий рядок для тестування. Тестування, тестування."
most_common = find_most_word(test_string)

print(f"Слово, що найчастіше зустрічається: '{most_common}'")