pool = {}

def thesaurus(*name):
    for i in name:
        first_character = i[:1]
        pool.setdefault(first_character,[])
        pool[first_character].append(i)
        
    return pool

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Мэри"))

