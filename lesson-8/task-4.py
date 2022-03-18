'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''
import math

production = 1
for n in range(1, 11):
    production *= n

print(production)

print('или')

print(math.factorial(10))
