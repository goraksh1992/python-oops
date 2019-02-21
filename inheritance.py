class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		# print("__init__ method class")
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first + "."+ self.last +"@example.com"  


	def pay_raise(self):
		self.pay = self.pay * Employee.raise_amount

	def fullname(self):
		return '{} {}'. format(self.first, self.last)


class Developer(Employee):
	def __init__(self, first, last, pay, prog_lang):
		# print("Developer sub class __init__ method class")
		super().__init__(first, last, pay) # call parent class init method
		self.prog_lang = prog_lang


class Manager(Employee):
	def __init__(self, first, last, pay, employee=None):
		# print("Manger sub class __init__ method class")
		super().__init__(first, last, pay)
		if employee is None:
			self.employee = []
		else:
			self.employee = employee

	def add_emp(self, emp):
		if emp not in self.employee:
			self.employee.append(emp)

	def remove_emp(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)

	def print_emp(self):
		for emp in self.employee:
			print('--->', emp.fullname())



dev_1 = Developer("gaurav", "sanas", 50000, "Python")
dev_2 = Developer("Amit", "Patil", 30000, "Java")

print(dev_1.email)
print(dev_1.prog_lang)

mgr_1 = Manager("Sunil", "Pal", 30000, [dev_1])

mgr_1.add_emp(dev_2)

print(mgr_1.print_emp())

print(mgr_1.remove_emp(dev_1))

print(mgr_1.print_emp())