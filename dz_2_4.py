persons = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
persons_len = int(len(persons))

i = 0
while i < persons_len:

    name_person = (persons[i].split(" ")[-1])
    name_person = name_person.title()
    print(f"Привет, {name_person}!")
    i += 1
