
class Person:

    def __init__(self, annual_salary):

        self.annual_salary = annual_salary
        self.hourly_rate = round(self.annual_salary / 52 / 5 / 8, 2)
        self.overtime_rate = round(self.hourly_rate * 1.5, 2)

