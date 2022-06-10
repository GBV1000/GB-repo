def even(num):
    for i in range(1, num + 1 , 2):
        #print(i)
        yield i

num = 15
gen = even(num)
for i in range(1, num + 1, 2):
    print(next(gen))
