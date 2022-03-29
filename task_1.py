# С клавиатуры вводится текст, определить, сколько в нём гласных, а сколько
# согласных. В случае равенства вывести на экран все гласные буквы.

text = input('Please type some text: ')
vowels= 0 #счетчик гласных
consonants = 0 #счетчик согласных
vowels_list = [] #массив гласных букв на случай если будет равное число гласных и согласных

for letter in text: #пробегаемся по тексту посимвольно
    if letter == ' ': #пропуск пробелов в тексте(пропускаем итерацию если набран пробел)
        continue
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y": # если гласная
        vowels_list.append(letter) #добавляем гласную букву в массив
        vowels += 1 #увеличиваем счетчик глассной
    else:
        consonants += 1 #увеличиваем счетчик согласных
if vowels == consonants:  #если количество гласных и согласных одинаково
    print(f'Vowels list: {vowels_list}') #выводим список гласных из текста
else:
    print(f'Vowels: {vowels} Consonants: {consonants}') #иначе выводим количество глассных и согласных


