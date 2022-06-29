def val_checker(x):
    def val_temp(fun):
        def wrapper(*args):
            for i in args:
                if i <= 0:
                    msg = f'wrong val: {i}'
                    raise ValueError(msg)
            return fun(i)
        return wrapper
    return val_temp


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x**3

# print(calc_cube(5))
# print(calc_cube(-5))
a = calc_cube(5)
print(a)
b = calc_cube(-5)
print(b)

#Надеюсь правильно понял с Traceback,можно было и красивее с исключением сообщение