class PayrollSystem:
    def calculate_payroll(self, employees):
        print("Calculating the payroll")
        print("===========")
        for employee in employees:
            print(f"{employee.id} - {employee.name}")
            print(f"Salary is, {employee.calculate_payroll()}")


class ProductivitySystem:
    def track(self, employees, hours):
        print("Tracking employees productivity")
        for employee in employees:
            employee.work(hours)
        print("*****")


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hour_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class DisgruntledEmployee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def calculate_payroll(self):
        return 10000


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')


salary_emp = SalaryEmployee(1, "heena", 2000)
hourly_emp = HourlyEmployee(2, "meeta", 12, 50)
commission_emp = CommissionEmployee(3, "palak", 1000, 250)
ps = PayrollSystem()
ps.calculate_payroll([salary_emp, hourly_emp, commission_emp])

print("****************")

salary_emp = SalaryEmployee(1, "heena", 2000)
hourly_emp = HourlyEmployee(2, "meeta", 12, 50)
commission_emp = CommissionEmployee(3, "palak", 1000, 250)
disgruntled_emp = DisgruntledEmployee(4, "Simran")
ps = PayrollSystem()
ps.calculate_payroll([salary_emp, hourly_emp, commission_emp, disgruntled_emp])


# class TemporarySecretary2(Secretary, HourlyEmployee):
#     pass

# class TemporarySecretary(HourlyEmployee, Secretary):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super.__init__(id, name, hours_worked, hour_rate)
#
#
# class TemporarySecretary2(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super.__init__(id, name, hours_worked, hour_rate)
        # HourlyEmployee.__init__(id, name, hours_worked, hour_rate)


class TemporarySecretary(Secretary, HourlyEmployee):
    def __init__(self, id, name, hours_worked, hour_rate):
        HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)

    def calculate_payroll(self):
        return HourlyEmployee.calculate_payroll(self)


print("$$$$$$$$$$$$$$$$")
manager = Manager(12, "Mary", 34000)
secretary = Secretary(13, "Joy", 2233)
sales_guy = SalesPerson(15, "raj", 1000, 250)
factory_worker = FactoryWorker(16, "atul", 40, 15)
temporary_secretary = TemporarySecretary2(5, 'Robin Williams', 40, 9)
employees_list = [manager, secretary, sales_guy, factory_worker, temporary_secretary]
productivity_system = ProductivitySystem()
productivity_system.track(employees=employees_list, hours=40)

payroll = PayrollSystem()
payroll.calculate_payroll(employees=employees_list)
