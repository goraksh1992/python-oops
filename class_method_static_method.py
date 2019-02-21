class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		print("__init__ method class")
		self.first = first
		self.last = last
		self.pay = pay


	def pay_raise(self):
		self.pay = self.pay * Employee.raise_amount

	# below method is class method and @classmethod is use for set as class method
	# this method change the class variable value
	@classmethod
	def set_raise_amt(cls, amt):
		cls.raise_amt = amt

	@classmethod
	def from_string(cls, string):
		first, last, pay = string.split("-")
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp = Employee("gaurav", "sanas", 50000)

# -------------------------------------------------
# before value change
print(emp.raise_amt)
print(Employee.raise_amt)

# here value change
print(Employee.set_raise_amt(1.05))

# after value change
print(Employee.raise_amt)
print(emp.raise_amt)

# ------------------------------------------------
#  use of string

emp_str_1 = "Amit-Patil-20000"

# first, last, pay = emp_str_1.split("-");

# emp2 = Employee(first, last, pay)

emp2 = Employee.from_string(emp_str_1)

print(emp2.first)
print(emp2.pay)


# print(Employee.raise_amt)
# print(emp2.raise_amt)

# splite function splite the string into list / array
# str1 = emp_str_1.split("-");
# print(str1) ['Amit', 'Patil', '20000']

# -------------------------------------------------

# static method call 

import datetime
my_date = datetime.date(2019, 2, 23)

print(Employee.is_workday(my_date));

# print(my_date.weekday())