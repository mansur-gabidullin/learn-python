'''
Задача 9

Найти максимальную цифру в числе

Пример:

    354359688

    'Цифра - 9 максимальная в числе 354359688'
'''

number = 354359688
max_digit = float('-inf')
digit = None
while number > 0:
    digit = number % 10
    number //= 10
    if digit > max_digit:
        max_digit = digit
print(max_digit)

print('или')

number = 354359688
print(max(map(int, str(number))))
