"""

Домашнее задание №2

Работа csv

* Создайте список словарей с ключами name, age и job
* Запишите содержимое списка словарей в файл в формате csv

"""
import random
import csv

NAMES = ['Сергей', 'Павел', 'Петр', 'Антон', 'Виталий', 'Анатолий', 'Алексей']
JOBS = ['программист', 'слесарь', 'менеджер', 'сантехник', 'электрик', 'педиатр', 'стоматолог']

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    people = [{'name':random.choice(NAMES), 'age':random.randint(23,65), 'job':random.choice(JOBS)} for _ in range(20)]
    fields = ['name', 'age', 'job']
    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        csv_file = csv.DictWriter(f, fields, delimiter=';')
        csv_file.writeheader()
        csv_file.writerows(people)

if __name__ == "__main__":
    main()
