class Employee:
	# __init__() method acts as contructor and it is call when instance get created
	def __init__(self, first, last, pay):
		print("__init__ method class")
		self.first = first
		self.last = last
		self.pay = pay

	# self parameter is compulsary when we create method
	def fullname(self):
		return '{} {}'. format(self.first, self.last) 

	@property
	def fullname(self):
		return '{} {}'. format(self.first, self.last)

	@fullname.setter
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first
		self.last = last

	@fullname.deleter
	def fullname(self):
		print("Name delete !")
		self.first = None
		self.last = None
	
emp = Employee("gaurav","sanas",50000)

# print(emp.fullname())

# when declare method as property so there is no need to add parenthesis "()" 
print(emp.fullname)

emp.fullname = "Arjun Pandit"

print(emp.first)
print(emp.last)
print(emp.fullname)

del emp.fullname

print(emp.first)
