#4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
#А также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы
# — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, 
#уникальные для каждого типа оргтехники.


class Storage:
	def __init__(self, total_places, used_places=0, storage_list=[]):
		self.total_places = total_places
		self.used_places = used_places
		self.storage_list = storage_list

	def add_to_storage(self, device):
		self.storage_list.append(device)
		self.used_places += 1
		print(f'{device.name} Добавлено .Свободный остаток - {self.total_places - self.used_places} .')


class Devices:
	def __init__(self, name, number):
		self.name = name
		self.number = number


class PC(Devices):
	def __init__(self, name, number, type_of_pc, brand, purpose):
		super().__init__(name, number)
		self.type_of_pc = type_of_pc
		self.brand = brand
		self.purpose = purpose

	def print_text(self, text):
		print(f'{text} {self.type_of_pc} {self.brand} for {self.purpose}.')


class Monitor(Devices):
	def __init__(self, name, number, diagonal, brand):
		super().__init__(name, number)
		self.diagonal = diagonal
		self.brand = brand

	def print_text(self, text):
		print(f'{text} {self.name} {self.diagonal} {self.brand}.')


if __name__ == "__main__":
	storage = Storage(200)
	pc = PC('laptop', '0011', 'laptop', 'hp', 'programmist')
	pc.print_text('Приобретен')
	monitor = Monitor('Monitor', '0361', '27"', 'HP')
	monitor.print_text('Потребность в закупке')
	storage.add_to_storage(pc)
	storage.add_to_storage(monitor)
