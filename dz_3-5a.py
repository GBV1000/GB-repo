import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num, more_repit , **source_dic):

    result = []

    try:
        for i in range(num):
            temp_str_result = ""

            for dict_from_source_dict in source_dic.values():
                word_choice = random.choice(dict_from_source_dict)

                if more_repit == 'no':
                    word_choice = dict_from_source_dict.pop(dict_from_source_dict.index(word_choice))
                temp_str_result += (f"{word_choice} ")

            result.append(temp_str_result)

        print(f"Кол-во комбинаций - {len(result)}\n")

    except:

        print(f"\nСлова исчерпаны, максимальное кол-во комбинаций - {len(result)}.")
        print("Выбирите 'Повторение слов' ->> yes\n")

    return result


num = int(input("Введите кол-во шуток - "))
more_repit = input("Повторение слов? yes/no - ")
'''
param "num" - numbers of jokes ('int class')
param "more_repit" - word uniqueness condition ('yes' or 'no')
param source_dic_N - source dictionaries for forming jokes
**source_dic - kwargs dict words
return: list of strings with random words from kwargs
'''

print(get_jokes(num, more_repit , source_dic_1 = nouns , source_dic_2 =adverbs ,source_dic_3 =adjectives ))
