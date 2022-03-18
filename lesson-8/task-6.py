'''
(!!!Подсказка на следующие 5 задач - превратите число в строку, а потом работайте с строкой)
Задача 6

Найти сумму цифр числа.

    Пример:

    254314

    Сумма цифр числа - 19(2+5+4+3+1+4)

'''

number = 254314
digit_sum = 0
for char in str(number):
    digit_sum += int(char)
print(digit_sum)

print('или')

print(sum(map(int, str(number))))
