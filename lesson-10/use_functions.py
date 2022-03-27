"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

# while True:
#     print('1. пополнение счета')
#     print('2. покупка')
#     print('3. история покупок')
#     print('4. выход')
#
#     choice = input('Выберите пункт меню')
#     if choice == '1':
#         pass
#     elif choice == '2':
#         pass
#     elif choice == '3':
#         pass
#     elif choice == '4':
#         break
#     else:
#         print('Неверный пункт меню')


QUESTION_CHOICE = 'Выберите пункт меню: '
QUESTION_REFILL_AMOUNT = 'Введите сумму на сколько пополнить счет: '
QUESTION_PURCHASE_COST = 'Введите сумму покупки: '
QUESTION_PURCHASE_NAME = 'Введите название покупки: '
MESSAGE_WRONG_ACTION_CHOICE = 'Неверный пункт меню'
MESSAGE_ESCAPE = 'До встречи!'
MESSAGE_REMAINING_AMOUNT = 'Денег не хватает!'
DESCRIPTION_OPEN = 'открытие счета'
DESCRIPTION_REFILL = 'пополнение счета'
DESCRIPTION_PURCHASE = 'покупка'
DESCRIPTION_HISTORY = 'история покупок'
DESCRIPTION_ESCAPE = 'выход'

FORMAT_PATTERN_LOG_HISTORY = '{:+.2f}: {}'
FORMAT_PATTERN_LOG_PURCHASE = '{}: {}'
FORMAT_PATTERN_MENU_ITEM = '{}. {}'

log = [(0, DESCRIPTION_OPEN)]


def refill(logger, get_remaining_amount=None):
    print()
    refill_amount = float(input(QUESTION_REFILL_AMOUNT))
    logger.append((refill_amount, DESCRIPTION_REFILL))


def purchase(logger, get_remaining_amount):
    print()
    remaining_amount = get_remaining_amount(logger)

    if remaining_amount == 0:
        print(MESSAGE_REMAINING_AMOUNT)
        return

    cost = float(input(QUESTION_PURCHASE_COST))

    if cost > remaining_amount:
        print()
        print(MESSAGE_REMAINING_AMOUNT)
        return

    print()
    purchase_name = input(QUESTION_PURCHASE_NAME)
    logger.append((-cost, FORMAT_PATTERN_LOG_PURCHASE.format(DESCRIPTION_PURCHASE, purchase_name)))


def history(logger, get_remaining_amount):
    print()
    remaining_amount = get_remaining_amount(logger)

    for amount, description in logger:
        print(FORMAT_PATTERN_LOG_HISTORY.format(amount, description))

    print('_' * 25)
    print(remaining_amount)


def escape(logger=None, get_remaining_amount=None):
    print()
    print(MESSAGE_ESCAPE)


def print_menu(items):
    print()
    for i, description in enumerate(items, 1):
        print(FORMAT_PATTERN_MENU_ITEM.format(i, description))


def generate_actions(refill_handler, purchase_handler, history_handler):
    return (
        (DESCRIPTION_REFILL, refill_handler),
        (DESCRIPTION_PURCHASE, purchase_handler),
        (DESCRIPTION_HISTORY, history_handler),
    )


def action_selector(actions, question):
    menu_items = (action[0] for action in actions)
    print_menu(menu_items)
    print()
    choice = int(input(question))
    actions_count = len(actions)

    if 0 < choice <= actions_count:
        return actions[choice - 1]


def amount_getter(logger):
    return sum((i[0] for i in logger))


def terminal(
        actions,
        select_action,
        escape_handler,
        logger,
        get_remaining_amount,
        choice_question=QUESTION_CHOICE,
        wrong_choice_message=MESSAGE_WRONG_ACTION_CHOICE
):
    running = True

    while running:
        action = select_action(actions + ((DESCRIPTION_ESCAPE, escape_handler),), choice_question)

        if not action:
            print()
            print(wrong_choice_message)
            continue

        handler = action[1]
        handler(logger, get_remaining_amount)

        if handler == escape_handler:
            running = False


terminal(generate_actions(refill, purchase, history), action_selector, escape, log, amount_getter)
