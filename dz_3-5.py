import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(num, more_repit = False, **source_dic):

    result = []

    try:
        for i in range(num):
            temp_str_result = ""

            for dict_from_source_dict in source_dic.values():
                word_choice = random.choice(dict_from_source_dict)

                if more_repit == False:
                    word_choice = dict_from_source_dict.pop(dict_from_source_dict.index(word_choice))
                temp_str_result += (f"{word_choice} ")

            result.append(temp_str_result)

        print(f"Кол-во комбинаций - {len(result)}\n")

    except:

        print(f"Слова исчерпаны, максимальное кол-во комбинаций - {len(result)}.")
        print("Измените значение more_repit\n")

    return result

'''
param arg - numbers of jokes ('int class')
param "more_repit" - word uniqueness condition (True or False)
param source_dic_N - source dictionaries for forming jokes
**source_dic - kwargs dict words
return: list of strings with random words from kwargs
'''



print(get_jokes(50, more_repit = False, source_dic_1 = nouns , source_dic_2 =adverbs ,source_dic_3 =adjectives ))
