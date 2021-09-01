
from General import Functions


class PayInfo:

    def __init__(self, salary, paycheck_list):

        self.salary = salary
        self.paycheck_list = paycheck_list

    def __str__(self):
        ret_str = "PayInfo:\n"
        ret_str += Functions.tab_str(self.salary, 1) + "\n"

        for i, paycheck in enumerate(self.paycheck_list):
            if i != 0:
                ret_str += "\n"
            ret_str += Functions.tab_str(str(paycheck), 1)
        return ret_str
