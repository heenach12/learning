# class methods and static methods

import datetime


class Employee:
    rais_amt = 1.05

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def fullname(self):
        return f"{self.name} email is {self.email}"

    @classmethod
    def set_raise_amt(cls, amount):
        cls.rais_amt = amount

    @classmethod
    def fromstring(cls, emp_str):
        name, pay = emp_str.split("-")
        return cls(name, pay)

    @staticmethod
    def get_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


e = Employee("Heena", "heena@gmail.com")
e.set_raise_amt(34)
print(e.rais_amt)
emp_str = "joy-25"
d = Employee.fromstring(emp_str)
print(d.fullname())


mydate = datetime.datetime(2019,4,2)
print(Employee.get_workday(mydate))

