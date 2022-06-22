"""
Написать скрипт, который выводит статистику для заданной папки в виде словаря,
в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
 а значения — общее количество файлов (в том числе и в подпапках),
  размер которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

dd if=/dev/zero of=setting.bin  bs=100  count=1
Излишние комментрии, сугубо для мя. Дабы, вспомнить, что делал.)
"""
import os.path

limits = [100, 1000, 10000, 100000] #в байтах

folder = 'some_data'

result = dict.fromkeys(limits, 0)

for adress, dirs, files in os.walk(folder): # https://pythoner.name/walk
    for file in files:

        x = os.stat(os.path.join(adress, file)).st_size

        for i in limits:
            if x == i:
                result[i] += 1

print('\t{')
for k, v in result.items():
    print('\t', f'{k}: {v}')
print('\t}')
