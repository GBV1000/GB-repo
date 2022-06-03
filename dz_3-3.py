pool = {}

def thesaurus(*name):
    for i in name:
        x=i[:1]
        pool.setdefault(x,[])
        pool[x].append(i)
        
    return pool

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Мэри"))

