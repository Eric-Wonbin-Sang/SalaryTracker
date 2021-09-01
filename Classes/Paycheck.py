
from General import Functions


class Paycheck:

    def __init__(self, parent_person, workweek_list, tax_group_list):

        self.parent_person = parent_person
        self.workweek_list = workweek_list
        self.tax_group_list = tax_group_list

    def __str__(self):
        ret_str = "Paycheck:\n"

        for i, workweek in enumerate(self.workweek_list):
            if i != 0:
                ret_str += "\n"
            ret_str += Functions.tab_str(str(workweek), 1)
        ret_str += "\n"

        for i, tax_group in enumerate(self.tax_group_list):
            if i != 0:
                ret_str += "\n"
            ret_str += Functions.tab_str(str(tax_group), 1)

        return ret_str
