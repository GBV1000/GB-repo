tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Ибрагим', 'Мистер Твистер', 'Алёша']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def even(tutors, klasses):
    for i in range(len(tutors)):

        if len(klasses) > i :
            pool = tuple((tutors[i],klasses[i]))
            yield pool
        else:
            pool = tuple((tutors[i],None))
            yield pool
    return pool

gen = even(tutors,klasses)
print(type(gen))
for i in range(1, len(tutors)):
    print(next(gen))
