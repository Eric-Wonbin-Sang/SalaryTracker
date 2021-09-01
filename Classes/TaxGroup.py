
from General import Functions


class TaxGroup:

    def __init__(self, parent_person, name, tax_list):

        self.parent_person = parent_person
        self.name = name
        self.tax_list = tax_list

    def __str__(self):
        ret_str = "TaxGroup:\n"
        ret_str += "\tname: {}\n".format(self.name)
        ret_str += "\ttax_list\n"

        for i, tax in enumerate(self.tax_list):
            if i != 0:
                ret_str += "\n"
            ret_str += Functions.tab_str(str(tax), 2)

        return ret_str
