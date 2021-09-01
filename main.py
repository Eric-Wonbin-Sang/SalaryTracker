import json

from Classes import PayInfo, Paycheck, WorkWeek, TaxGroup, Tax, Salary

from General import Constants


def get_salary(salary_dict):
    return Salary.Salary(
        annual_salary=salary_dict["annual_salary"]
    )


def get_pay_info_list(pay_info_dict_list):
    pay_info_list = []
    for pay_info_dict in pay_info_dict_list:
        salary = get_salary(pay_info_dict["salary_dict"])
        pay_info_list.append(
            PayInfo.PayInfo(
                salary=salary,
                paycheck_list=get_paycheck_list(pay_info_dict["paycheck_dict_list"], salary)
            )
        )
    return pay_info_list


def get_paycheck_list(pay_info_dict_list, salary):
    return [
        Paycheck.Paycheck(
            parent_person=salary,
            workweek_list=get_workweek_list(paycheck_dict["workweek_list"], salary),
            tax_group_list=get_tax_group_list(paycheck_dict["tax_group_list"], salary)
        ) for paycheck_dict in pay_info_dict_list
    ]


def get_workweek_list(workweek_dict_list, salary):
    return [
        WorkWeek.WorkWeek(
            parent_person=salary,
            start_dt=workweek_dict["start_dt"],
            end_dt=workweek_dict["end_dt"],
            base_hours=workweek_dict["base_hours"],
            overtime_hours=workweek_dict["overtime_hours"]
        ) for workweek_dict in workweek_dict_list
    ]


def get_tax_group_list(tax_group_dict_list, salary):
    return [
        TaxGroup.TaxGroup(
            parent_person=salary,
            name=tax_group_dict["name"],
            tax_list=get_tax_list(tax_group_dict["tax_list"], salary)
        ) for tax_group_dict in tax_group_dict_list
    ]


def get_tax_list(tax_dict_list, salary):
    return [
        Tax.Tax(
            parent_person=salary,
            name=tax_dict["name"],
            value=tax_dict["value"]
        ) for tax_dict in tax_dict_list
    ]


def main():

    pay_info_list = get_pay_info_list(json.load(open(Constants.paychecks_json)))

    for pay_info in pay_info_list:
        print(pay_info)


if __name__ == '__main__':
    main()
