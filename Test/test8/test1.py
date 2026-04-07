def repeat_message(message, times):
    for i in range(times):
        print(message)

repeat_message("Привіт!", 3)

# 2 варіант

def repeat_message_s(message, times):
    print((message + '\n') * times)

repeat_message_s("Привіт!", 3)

# 3 варіант

def repeated_message(message, times):
        return message * times

my_string = repeated_message("Привіт! ", 3)
print(my_string)

# 4 варіант
def repeated_message_join(message, times):
    list_of_messages = [message] * times
    return ' '.join(list_of_messages)

my_string = repeated_message_join("Привіт!", 3)
print(my_string)