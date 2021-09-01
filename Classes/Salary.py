
class Salary:

    def __init__(self, annual_salary):

        self.annual_salary = annual_salary
        self.hourly_rate = round(self.annual_salary / 52 / 5 / 8, 2)
        self.overtime_rate = round(self.hourly_rate * 1.5, 2)

    def __str__(self):
        ret_str = "Salary:\n"
        ret_str += "\tannual_salary: {}\n".format(self.annual_salary)
        ret_str += "\thourly_rate: {}\n".format(self.hourly_rate)
        ret_str += "\tovertime_rate: {}".format(self.overtime_rate)
        return ret_str
