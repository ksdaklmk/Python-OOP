class Car():
	
	def __init__(self, maker, year):
		self.maker = maker
		self.year = year
		self.status = 'dirty'
		
	def clean(self):
		print('... cleaning the car! ...')
		self.status = 'clean'
		

my_car = Car('Honda', 2020)
print(my_car.maker)
print(f'The car is in {my_car.status} status')
my_car.clean()
print(f'The car is now in {my_car.status} status')
