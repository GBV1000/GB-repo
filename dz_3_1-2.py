dict_num = {'zero': 'ноль','one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate_adv(num):
    if num.istitle():
        print(dict_num.get(num.lower(),'Данное значение отсутствует').title())
    else:
        print(dict_num.get(num.lower(),'Данное значение отсутствует'))

num = input('Напиши число от 1 до 10 на eng. (Прим. one, Zero)\n')
num_translate_adv(num)
