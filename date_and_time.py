"""

Домашнее задание №2

Дата и время

* Напечатайте в консоль даты: вчера, сегодня, месяц назад
* Превратите строку "01/01/17 12:10:03.234567" в объект datetime

"""

import datetime

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    today = datetime.datetime.now()
    day = datetime.timedelta(days = 1)
    print(today - day)
    print(today)
    previous_month = today.replace(day = 1) - datetime.timedelta(days = 1)
    try:
        previous_month = previous_month.replace(day = today.day)
    except ValueError:
        pass
    print(previous_month)

    
    
def str_2_datetime(string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.datetime.strptime(string, '%m/%d/%y %H:%M:%S.%f')

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/17 12:10:03.234567"))
