import random

print ('''Birthday Paradox
By Al Sweigart
Solution by Tony Fuentes''')

try:
    number_of_birthdays = int(input('How many birthdays shall I generate?: '))
except ValueError:
    print('Invalid input, please enter a number.')

def generate_birthdays():
    birthday = random.randint(1, 366)
    return birthday
    
birthday_list = []

for i in range(number_of_birthdays):
    birthday_list.append(generate_birthdays())

print(birthday_list)