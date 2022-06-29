def type_logger(func):
    def wrapper(*args):
        result = {}
        for i in args:
            result[i] = type(i)
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


print(calc_cube(7))

print(calc_cube(12,26,36.4,0.4,'j'))

print('\n')
print('второй вариант\n')


def type_logger(func):
    def wrapper(**args):
        result = {}
        for key, value in args.items():
            result[value] = type(value)
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


print(calc_cube(index=7))

print(calc_cube(index=12,index1=26,index2=36.4,index3=0.4,index4='j'))