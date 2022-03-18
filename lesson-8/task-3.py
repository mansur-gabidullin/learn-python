'''
Задача 3

Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

my_sum = 0
for n in range(1, 101):
    my_sum += n
print(my_sum)

print('или')

print(sum(range(1, 101)))
