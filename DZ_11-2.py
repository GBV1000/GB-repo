#2. Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных, вводимых
#пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с
#ошибкой.


class Zero_no(Exception):
    def __init__(self, text):
        self.text = text

def fun_delenie(first_num=0, second_num=0):
        first_num = int(input('Ввдите первое число - '))
        second_num = int(input('Ввидете второе число - '))
        if second_num == 0:
            raise Zero_no('Ошибка, деление на ноль запрещено')
        else:
            result = first_num/second_num
            print(f'Результат =  {result}')

try:
    fun_delenie()
except Zero_no as err:
    print(err)
