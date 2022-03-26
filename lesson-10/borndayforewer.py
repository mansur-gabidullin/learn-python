"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
#
# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')

TITLE = 'Тест Пушкина'
QUESTION_PUSHKIN_YEAR = 'Введите год рождения А.С.Пушкина: '
QUESTION_PUSHKIN_DAY = 'В какой день июня родился Пушкин?: '
PUSHKIN_BIRTH_YEAR = '1799'
PUSHKIN_BIRTH_DAY = '6'
MESSAGE_CORRECT = 'Верно'
MESSAGE_WRONG = 'Не верно'


def test(ask, correct_answer, on_wrong_message=MESSAGE_WRONG):
    answer = ask()
    while answer and answer != correct_answer:
        print(on_wrong_message)
        answer = ask()
    return bool(answer)


def test_pushkin():
    return all([
        test(lambda: input(QUESTION_PUSHKIN_YEAR), PUSHKIN_BIRTH_YEAR),
        test(lambda: input(QUESTION_PUSHKIN_DAY), PUSHKIN_BIRTH_DAY)
    ])


def print_message(message):
    print()
    print('*' * 100)
    print('{:*^100}'.format(f' {message} '))
    print('*' * 100)
    print()


print_message(TITLE)

if test_pushkin():
    print_message(MESSAGE_CORRECT)
else:
    print_message(MESSAGE_WRONG)
