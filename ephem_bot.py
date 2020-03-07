"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import datetime
import string
import settings
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)

PLANETS = {'Mercury':ephem.Mercury, 
             'Venus':ephem.Venus, 
              'Mars':ephem.Mars, 
           'Jupiter':ephem.Jupiter, 
            'Saturn':ephem.Saturn, 
            'Uranus':ephem.Uranus, 
           'Neptune':ephem.Neptune, 
             'Pluto':ephem.Pluto, 
               'Sun':ephem.Sun, 
              'Moon':ephem.Moon, }

def get_num_ending(number, array):
    # array массив слов или окончаний для чисел (1, 4, 5)
    number = number % 100
    if number >= 11 and number <= 19:
        return array[2]
    else:
        i = number % 10
        if i == 1:
            return array[0]
        elif i > 1 and i <= 4:
            return array[1]
        else:
            return array[2]


def get_count_words(text):
    for char in string.punctuation:
        while char in text:
            text = text.replace(char, ' ')
    return len(text.split())


def greet_user(bot, update):
    text = 'Вызван /start'
    update.message.reply_text(text)


def get_planet(bot, update):
    answer = 'Не знаю такую планету'
    today = datetime.datetime.now().strftime('%Y/%d/%m')
    planet_name = update.message.text.split()
    if len(planet_name) > 1 and planet_name[1].capitalize() in PLANETS:
        planet = PLANETS[planet_name[1].capitalize()](today)
        update.message.reply_text('{} :: {}'.format(today, ephem.constellation(planet)))
    else:
        update.message.reply_text(answer)


def count_words(bot, update):
    user_input = update.message.text.split()
    if len(user_input) > 1:
        cnt_words = get_count_words(' '.join(user_input[1:]))
        update.message.reply_text(f'Вы ввели {cnt_words} {get_num_ending(cnt_words,["слово","слова","слов"])}')    
    else:
        update.message.reply_text('Вы ввели 0 слов')

def next_full_moon(bot, update):
    today = datetime.datetime.now()
    user_input = update.message.text.split()
    if len(user_input) > 1:
        date_user = user_input[1]
        try:
            date_user = datetime.datetime.strptime(date_user, '%d.%m.%Y')
            date_full_moon = ephem.next_full_moon(date_user)
            delta_days = date_full_moon.datetime() - today
            count_days_word = get_num_ending(delta_days.days, ["день","дня","дней"])
            nearest_full_moon = date_full_moon.datetime().strftime("%d.%m.%Y")
            update.message.reply_text(f'Ближайшее полнолуние {nearest_full_moon}, осталось {delta_days.days} {count_days_word}')
        except ValueError:
            update.message.reply_text('Дата указана неверно, попробуйте в формате ДД.ММ.ГГГГ')
    else:
        date_full_moon = ephem.next_full_moon(today)
        delta_days = date_full_moon.datetime() - today
        count_days_word = get_num_ending(delta_days.days, ["день","дня","дней"])
        nearest_full_moon = date_full_moon.datetime().strftime("%d.%m.%Y")
        update.message.reply_text(f'Ближайшее полнолуние {nearest_full_moon}, осталось {delta_days.days} {count_days_word}')


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.BOT_TOKEN, request_kwargs=settings.PROXY)    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", get_planet))
    dp.add_handler(CommandHandler("wordcount", count_words))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
