#-*- coding: UTF-8 -*-
x = input()
d = x.split(' ')
d.append(' ')

if d[0] == 'show':
    with open('bakery.csv', 'r', encoding='UTF-8') as bakery:

        for line in bakery:
            print(line.strip())
else:
    with open('bakery.csv', 'r', encoding='UTF-8') as bakery:
        t = {}

        for i, j in enumerate(bakery):
            t[i] = j.splitlines()
            print((t))

        for key in t.keys():
            print(key)
            if d[1]==' ':

                if int(d[0])-1 <= key:
                    print(t[key])

            else:
                if int(d[0])-1 <= key <= int(d[1])-1:
                    print(t[key])

