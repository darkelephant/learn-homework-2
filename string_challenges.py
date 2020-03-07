# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
tmp = 'аеёиоуыэюя'
counter = sum([1 for char in word if char.lower() in tmp])
print(counter)


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
words = sentence.split()
avg_len_word = sum([len(word) for word in words]) / len(words)
print(avg_len_word)
