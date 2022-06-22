"""Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками»
в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены
в родительских папках (они играют роль пространств имён); предусмотреть возможные
исключительные ситуации; это реальная задача, которая решена, например, во фреймворке django.
-----------------------
Излишние комментрии, сугубо для мя. Дабы, вспомнить, что делал.)
-----------------------
"""

import shutil
import os.path

main_dir = 'my_project'
output_pattern = 'templates'
new_in_main_templates = os.path.join(main_dir, output_pattern) #создаем путь  my_project/templates

if not os.path.exists(new_in_main_templates): #если папки templates в пути my_project/templates нет, создаем. Иначе пропускаем
    os.mkdir(new_in_main_templates)

for address, dirs, files in os.walk(main_dir): # https://pythoner.name/walk

    if len(dirs) > 0:
        try:
            if dirs[0] == 'templates':
                print(os.path.join(address, dirs[0]))
                shutil.copytree(os.path.join(address, dirs[0]), new_in_main_templates, dirs_exist_ok=True) #copy my_project/authapp/templates в my_project/templates
        except:
            print('end')