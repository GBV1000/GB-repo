x = str(input("Введите выручку вида 5001,1 - "))
d = x.strip().split(',')
with open('bakery.csv', 'a', encoding='UTF-8') as bakery:
        print(f'{d[0]},{d[1]}\n', file=bakery)