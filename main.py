import json

from Classes import Paycheck, WorkWeek, TaxGroup, Tax, Person

from General import Constants


def get_person(person_dict):
    return Person.Person(
        annual_salary=person_dict["annual_salary"]
    )


def get_paycheck_list(paycheck_dict_list, person):

    return [
        Paycheck.Paycheck(
            parent_person=person,
            workweek_list=[
                WorkWeek.WorkWeek(
                    parent_person=person,
                    start_dt=workweek_dict["start_dt"],
                    end_dt=workweek_dict["end_dt"],
                    base_hours=workweek_dict["base_hours"],
                    overtime_hours=workweek_dict["overtime_hours"]
                ) for workweek_dict in paycheck_dict["workweek_list"]
            ],
            tax_group_list=[
                TaxGroup.TaxGroup(
                    parent_person=person,
                    name=tax_group_dict["name"],
                    tax_list=[
                        Tax.Tax(
                            parent_person=person,
                            name=tax_dict["name"],
                            value=tax_dict["value"]
                        ) for tax_dict in tax_group_dict["tax_list"]
                    ]
                ) for tax_group_dict in paycheck_dict["tax_group_list"]
            ]
        ) for paycheck_dict in paycheck_dict_list
    ]


def main():

    for pay_info_dict in json.load(open(Constants.paychecks_json)):
        person = get_person(pay_info_dict["person_dict"])
        paycheck_list = get_paycheck_list(pay_info_dict["paycheck_dict_list"], person)
        for paycheck in paycheck_list:
            print(paycheck)


if __name__ == '__main__':
    main()
