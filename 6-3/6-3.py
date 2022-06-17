import os.path

with open('names.csv', 'r', encoding='UTF-8') as name_temp:
    name_list = []
    for i in name_temp:
        temp_rip = " ".join(i.strip().split(','))
        name_list.append(temp_rip)

with open('hobby.csv', 'r', encoding='UTF-8') as hobby_temp:
    hobby_list = []

    for t in hobby_temp:
        dd = t.strip()
        hobby_list.append(dd)

pool = {}

if  len(name_list) < len(hobby_list):
    raise SystemExit(1)

for i in range(len(name_list)):

    if len(hobby_list) > i:
        pool[name_list[i]]=hobby_list[i]

    else:
        pool[name_list[i]] = 'None'
print(pool)

with open('result.txt', 'w', encoding='UTF-8') as result:
    for i in pool:
        print(f'{i},{pool[i]}', file=result)
