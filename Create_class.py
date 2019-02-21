class Employee:
	# __init__() method acts as contructor and it is call when instance get created
	def __init__(self, first, last, pay, mail):
		print("__init__ method class")
		self.first = first
		self.last = last
		self.pay = pay
		self.mail = mail

	# self parameter is compulsary when we create method
	def fullname(self, fname, lname):
		# return '{} {}'. format(fname, lname)
		return '{} {}'. format(self.first, self.last) 



emp = Employee("gaurav","sanas",50000,"gaurav@example.com")

print(emp.fullname("sanas","gaurav"))