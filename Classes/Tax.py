
class Tax:

    def __init__(self, parent_person, name, value):

        self.parent_person = parent_person
        self.name = name
        self.value = value

    def __str__(self):
        ret_str = "Tax:\n"
        ret_str += "\tname: {}\n".format(self.name)
        ret_str += "\tvalue: {}".format(self.value)
        return ret_str
