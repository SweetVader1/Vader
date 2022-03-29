


# Вводится 2 числа с клавиатуры (от 1 до 20). Так же генерируется 2 числа рандомно.
# Посчитать, сколько раз пара введенных чисел с клавиатуры окажется больше
# рандомной пары. Проверку выполнить 7 раз.
# В случае равенства (количества, когда пара больше и всех остальных случаем)
# вывести случайные числа, полученные в 4 итерации.

from random import randint

first_num = int(input('Enter numder A from 1 to 20: '))
second_num = int(input('Enter numder B from 1 to 20: '))
num_sum = sum([first_num, second_num]) #сумма введенных с клавиатуры чисел
num_list = [] #переменная для хранения рандомных чисел из 4 иетрации
i = 0
counter = 0

while(i < 7):
    first_random = randint(1, 20) #генерация рандомного числа
    second_random = randint(1, 20) #генерация рандомного числа
    random_sum = sum([first_random, second_random]) #их сумма
    if num_sum > random_sum: #если сумма введенных больше суммы рандомных
        print('more') #принт для наглядности что бы каждая итерация была видна в консоли
        counter += 1 #увеличиваем счетчик если сумма введенных больше
    else:
        print('less') #принт для наглядности что бы каждая итерация была видна в консоли
    if i == 3: #четвертая итерация на ней надо записать рандомные числа в список
        num_list.append(first_random)
        num_list.append(second_random)
    i += 1 #увеличиваем счечик итераций что бы цикл остановился на условии i < 7

if counter > 3: #в условии сказано 7 проверок, значит 4 проверки это уже больше половины
    print(f'Fourth iteration random numbers: {num_list}')



# Посчитать, сколько раз встречается определенная цифра в числах. Количество
# введенных чисел и искомая цифра задаются с клавиатуры. Числа выбираются
# рандомно.

desired_figure = input('Enter desired figure: ') #искомое число
iter_count = int(input('Type number of checks: ')) #количество проверок
check_number = 0 #номер проверки

while check_number < iter_count: #пока номеро проверки меньше введенного количества проверок
    if int(desired_figure) > 9: #если число больше 9 т.е. неверное, остановливаем программу
        print('Incorrect figure')
        break
    counter = 0 #счетчик совпадений цифры в числе
    number = input('Please enter the number: ') #вводим рандомное число
    for sym in number: # т.к. введенный инпут всегда строка то пробегаемся по ней посимвольно без преобразований
        if sym == desired_figure: #если символ совпадает с тем что мы ввели вначале увеличиваем счетчик совпадений
            counter += 1
    print(f'The number of matches in the number: {counter}')
    check_number += 1 #увеличиваем счетчик проверок что бы остановить цикл когда условие while будет false, т.е. счетчик превысит количество введенных проверок


