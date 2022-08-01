#5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём 
#оргтехники на склад и передачу в определённое подразделение компании. Для хранения данных 
#о наименовании и количестве единиц оргтехники, а также других данных, можно использовать 
#любую подходящую структуру (например, словарь).



from DZ_11_4 import *


class Departament(Storage):
	def __init__(self, total_places, departament):
		super().__init__(total_places, used_places=0, storage_list=[])
		self.departament = departament
		self.departament_allocation = {}

	def add_to_storage(self, device, departament):
		self.departament_allocation.setdefault(self.departament, device.name)
		print(f'{device.name} место расположения {self.departament}.')
		print(self.departament_allocation)


pc = PC('laptop', '0011', 'laptop', 'hp', 'programmist')
monitor = Monitor('Monitor', '0361', '27"', 'HP')

dep_1 = Departament(15, 'Фриланс')
dep_1.add_to_storage(pc, 'Фриланс')
dep_2 = Departament(15, 'Головной офис')
dep_2.add_to_storage(monitor, 'Головной офис')
