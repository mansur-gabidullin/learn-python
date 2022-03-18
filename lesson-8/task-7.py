'''
Задача 7

Найти произведение цифр числа.

    Пример:

    254314

    Произведение цифр числа - 480(2*5*4*3*1*4)
'''
from math import prod

number = 254314
digit_production = 1
for char in str(number):
    digit_production *= int(char)
print(digit_production)

print('или')

print(prod(map(int, str(number))))
