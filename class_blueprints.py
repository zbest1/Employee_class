#Python OOP

import datetime

####################################################################################

class Employee():
	
	num_of_emps = 0
	raise_amt = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		#self.email = first + '.' + last + '@company.com'
		
		Employee.num_of_emps += 1
	
	@property
	def email(self):
		'''
		We are defining our e-mail as if it is a method 
		but we can now access it as if it is an atributte.
		'''
		return '{}.{}@email.com'.format(self.first, self.last)
	
	@property
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
	@fullname.setter
	def fullname(self, name):
		'''
		Now in case a different full name is given after an instance is created 
		the email last and first name will automaticaly be updated.
		'''
		first, last = name.split(' ')
		self.first = first
		self.last = last
	
	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None
	
	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)
	
	def __repr__(self):
		return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)
	
	def __str__(self):
		return '{} - {}'.format(self.fullname(), self.email)
	
	def __add__(self, other):
		"""
		A special method created inorder to add two employees and get their
		combined salary.
		"""
		return self.pay + other.pay
	
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount
	
	@classmethod
	def from_string(cls, emp_str):
		"""Parse string like employees."""
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)
	
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

####################################################################################

class Developer(Employee):
	raise_amt = 1.10

	#add programming language atribute.
	def __init__(self, first, last, pay, prog_lang):
		#super().__init__(first, last, pay) for python 3
		Employee.__init__(self, first, last, pay)
		self.prog_lang = prog_lang

####################################################################################

class Manager(Employee):
	
	#list of employees that this manager manages.
	
	def __init__(self, first, last, pay, employees=None):
		#super().__init__(first, last, pay) for python 3
		Employee.__init__(self, first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees
	
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
	
	def print_emps(self):
		for emp in self.employees:
			print(emp.__dict__)

####################################################################################

runmode = 1

if runmode == 1:
	
	my_date = datetime.date(2018, 7, 10)
	print(Employee.is_workday(my_date))

	print(Employee.raise_amt)
	emp1 = Employee('Kwstas', 'Rouvalis', 50000)
	emp2 = Employee('Martin', 'Sinanis', 50000)
	emp_str_1 = 'Giwrgos-Nanos-70000'
	emp3 = Employee.from_string(emp_str_1)

	print('Emp1 pay is {}'.format(emp1.pay))
	emp1.apply_raise()
	print('Emp1 pay after raise is {}'.format(emp1.pay))

	Employee.set_raise_amt(1.50)
	print('Emp2 pay is {}'.format(emp2.pay))
	emp2.apply_raise()
	print('Emp2 pay after raise (for new raise amount) is {}'.format(emp2.pay))
	
	emp4 = Employee('Thanos', 'Pnts', 30000)
	emp4.fullname = 'Thanos Pantos'
	
	print(emp4.first)
	print(emp4.email)
	print(emp4.fullname)
	
	del emp4.fullname

elif runmode == 2:
	
	dev1 = Developer('Kwstas', 'Rouvalis', 50000, 'Python')
	dev2 = Developer('Martin', 'Sinanis', 50000, 'Java')
	
	print(dev1.pay)
	dev1.apply_raise()
	print(dev1.pay)

elif runmode == 3:
	
	#print(help(Developer))
	print(isinstance(mgr_1, Developer))
	print(issubclass(Manager, Developer))
	
	dev1 = Developer('Kwstas', 'Rouvalis', 50000, 'Python')
	dev2 = Developer('Martin', 'Sinanis', 50000, 'Java')
	
	mgr_1 = Manager('Babis', 'Papadimitriou', '90000', [dev1])
	
	mgr_1.add_emp(dev2)
	
	mgr_1.print_emps()
	
