"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""
import string


def count_words(text):
    for char in string.punctuation:
        while char in text:
            text = text.replace(char, ' ')
    return len(text.split())


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding='utf8') as input_file:
        text = input_file.read()
    print(f"Длина строки {len(text)}")
    print(f"Количество слов {count_words(text)}")
    with open('referat2.txt', 'w', encoding='utf8') as output_file:
        output_file.write(text.replace('.','!'))


if __name__ == "__main__":
    main()
