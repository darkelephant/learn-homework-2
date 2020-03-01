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
    while '  ' in text:
        text = text.replace('  ', ' ')
    return len(text.split())

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    input_file = open('referat.txt', 'r', encoding='utf8')
    text = input_file.read()
    input_file.close()
    print(f"Длина строки {len(text)}")
    print(f"Количество слов {count_words(text)}")
    output_file = open('referat2.txt', 'w', encoding='utf8')
    output_file.write(text.replace('.','!'))
    output_file.close()

if __name__ == "__main__":
    main()
