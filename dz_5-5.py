src = [300,2,12,44,1,1,4,10,7,1,78,123,55]

def gen_nums(src):
    result = []
    #result = [second_num  for first_num, second_num in zip(src, src[1:]) if first_num < second_num]
    for first_num,second_num in zip(src, src[1:]):
        if first_num < second_num:
            result.append(second_num)
    return  result

print(gen_nums(src))
