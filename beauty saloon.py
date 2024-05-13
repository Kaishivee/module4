from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.prompt import Confirm
from rich.columns import Columns
from rich import print

console = Console()

name_ = []
items = []
time_ = []
date_ = []
cost_ = []


def info():
    procedure = input('На какую процедуру хотели бы записаться?'
                      '(маникюр/педикюр/СПА/стрижка: ')
    day = input('На какой день записываетесь? ')
    start_time = input('В какое время Вам удобно подойти? ')
    client = input('Уточните Ваше имя: ')
    cost = int(input('Уточните цену процедуры: '))
    items.append(procedure)
    date_.append(day)
    time_.append(start_time)
    name_.append(client)
    cost_.append(cost)


def check_price():
    console.print(Panel(
        Text(
            f'''
        Маникюр - 1300 ₽
        Педикюр - 1500 ₽
        СПА - 2000 ₽
        Стрижка - 800 ₽
            '''
        ),
        title='Price',
        width=34
    ))


def check_params():
    global items
    global date_
    global time_
    global name_
    items_panel = Panel(
        Text('\n'.join([f'{items}' for items in items])),
        title='Название процедуры',
        width=34
    )
    date_panel = Panel(
        Text('\n'.join([f'{date_}' for date_ in date_])),
        title='Дата записи',
        width=34
    )
    time_panel = Panel(
        ('\n'.join([f'{time_}' for time_ in time_])),
        title='Время записи',
        width=34
    )
    name_panel = Panel(
        Text('\n'.join([f'{name_}' for name_ in name_])),
        title='На запись придет',
        width=34
    )

    all_panel = Columns([name_panel, items_panel, date_panel, time_panel])
    console.print(all_panel)


def cancel_appointment():
    name_.clear()
    items.clear()
    time_.clear()
    date_.clear()
    console.print('Ваша запись отменена! ')


def create_check():
    total_price = sum([int(i) for i in cost_])
    salon_name = 'Stilnyashka'
    console.print(Panel(
        Text(
            f'''
           Запись успешно завершена!
               Будем Вас ждать!
           ___________________________
           Клиент: {name_}
           Процедура: {items}
           Дата записи: {date_}
           Время записи: {time_}
           Общая цена: {total_price} ₽
           Название салона: {salon_name}

                   ''',
        ),
        title='Чек',
        width=50
    ))


def run():
    console.print(Panel(Text(
        '''  Добро пожаловать в салон 
        Stilnyashka! 
    1. Записаться на процедуру
    2. Посмотреть прайс
    3. Проверить запись
    4. Отменить запись
    5. Создать чек
    6. Завершить работу '''),
        title='Beauty saloon',
        width=34
    ))
    while True:
        print()
        oper = console.input('Что хочешь сделать? (1-6) ')
        if oper == '1':
            info()
        elif oper == '2':
            check_price()
        elif oper == '3':
            check_params()
        elif oper == '4':
            cancel_appointment()
        elif oper == '5':
            create_check()
        elif oper == '6':
            if Confirm.ask('Вы действительно хотите выйти? '):
                break
        else:
            console.print('Что-то не то!')


run()
