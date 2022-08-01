#1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год». 
#В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и 
#преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
#и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


from datetime import datetime


class Data:
	def __init__(self, date_data):
		self.date_data = date_data

	@classmethod
	def get_in_date(cls, date_data):
		d, m, y = [int(i) for i in date_data.split('-')]
		return d, m, y

	@staticmethod
	def valid_date(date_data):
		try:
			datetime.strptime(date_data, '%d-%m-%Y')
		except ValueError:
			print('Ошибка входящих данных, не соответствует формату/значению')
			raise ValueError("Формат/значение, не соответствует дате, прим.( DD-MM-YYYY)")


print(Data.get_in_date('07-07-2022'))
print(Data.valid_date('31-13-2022'))
