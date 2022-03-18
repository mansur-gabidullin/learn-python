'''
Задача 10

Найти количество цифр 5 в числе

    Пример:

        543231235643

        'В числе 2 5-ки.'
'''

number = 543231235643
count = 0
while number > 0:
    if number % 10 == 5:
        count += 1
    number //= 10

print('В числе', count, '5-ки.')

print('или')

number = 543231235643
print(f"В числе {list(str(number)).count('5')} 5-ки.")
