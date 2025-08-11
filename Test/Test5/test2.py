from collections import namedtuple

Participant = namedtuple('Participant', ['first_name', 'last_name', 'school', 'score'])

participant1 = Participant('Іван', 'Іваненко', 'Школа №333', 95)
print(participant1)
print(f"Ім'я: {participant1.first_name}")
print(f"Школа: {participant1.school}")