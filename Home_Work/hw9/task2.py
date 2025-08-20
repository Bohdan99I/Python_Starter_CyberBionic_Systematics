def is_palindrome(text):    
    cleaned = ''.join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


while True:
    phrase = input("Введіть фразу для перевірки (або 'stop' для виходу): ")
    if phrase.lower() == "stop":
        print("Програму завершено.")
        break
    if is_palindrome(phrase):
        print("✅ Це паліндром!")
    else:
        print("❌ Це не паліндром.")
