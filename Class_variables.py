class Employee:

	num_of_emp = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		print("__init__ method class")
		self.first = first
		self.last = last
		self.pay = pay

		Employee.num_of_emp += 1

	def pay_raise(self):
		self.pay = self.pay * Employee.raise_amount


print(Employee.num_of_emp)

emp = Employee("gaurav", "sanas", 50000)

print(Employee.num_of_emp)

print(emp.pay)
emp.pay_raise()
print(emp.pay)