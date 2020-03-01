from collections import Counter
# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
c = Counter([x['first_name'] for x in students])
for key, value in c.items():
    print(f'{key}: {value}')

# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
c = Counter([x['first_name'] for x in students])
print(c.most_common(1)[0][0])

# Пример вывода:
# Самое частое имя среди учеников: Маша

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
for number, students in enumerate(school_students):
    c = Counter([x['first_name'] for x in students ])
    print(f'Самое частое имя в классе {number+1}: {c.most_common(1)[0][0]}')

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
for classes in school:
    stat = {'male':0, 'female':0}
    for student in classes['students']:
        if is_male[student['first_name']]:
            stat['male'] += 1
        else:
            stat['female'] += 1
    print(f'# В классе {classes["class"]} {stat["female"]} девочки и {stat["male"]} мальчика')
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}

max_male = {'class':'', 'count':0}
max_female = {'class':'', 'count':0}

for classes in school:
    stat = {'male':0, 'female':0}
    for student in classes['students']:
        if is_male[student['first_name']]:
            stat['male'] += 1
        else:
            stat['female'] += 1

    if stat['male'] > max_male['count']:
        max_male['count'] = stat['male']
        max_male['class'] = classes['class']

    if stat['female'] > max_female['count']:
        max_female['count'] = stat['female']
        max_female['class'] = classes['class']

print(f'Больше всего мальчиков в классе {max_male["class"]}')
print(f'Больше всего девочек в классе {max_female["class"]}')
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a