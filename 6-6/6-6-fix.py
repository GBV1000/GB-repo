from sys import argv

read_param = argv[:]

read_param =read_param[1:]

with open('bakery.csv', 'r', encoding='utf-8') as bakery:

        t={}
        for i, j in enumerate(bakery):
            t[i] = j.splitlines()

        for key in t.keys():

            if argv[1] == 'show':
                print(t[key])

            elif len(argv) == 2:
                if int(argv[1])-1 <= key:
                    print(t[key])

            else:
                if int(argv[1])-1 <= key <= int(argv[2])-1:
                    print(t[key])
