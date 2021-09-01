
class WorkWeek:

    def __init__(self, parent_person, start_dt, end_dt, base_hours, overtime_hours):

        self.parent_person = parent_person
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.base_hours = base_hours
        self.overtime_hours = overtime_hours

    def __str__(self):
        ret_str = "WorkWeek:\n"
        ret_str += "\tstart_dt: {}\n".format(self.start_dt)
        ret_str += "\tend_dt: {}\n".format(self.end_dt)
        ret_str += "\tbase_hours: {}\n".format(self.base_hours)
        ret_str += "\tovertime_hours: {}".format(self.overtime_hours)
        return ret_str
