src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def even(src):

    unic_num = set()
    temp_num = set()
    result = []
    for i in src:
       if i not in temp_num:
            unic_num.add(i)
       else:
            unic_num.discard(i)
       temp_num.add(i)

    for i in src:
        if i in unic_num:
            result.append(i)
    return result

print(even(src))
