import typing


class Department:

    def __init__(self, name: str, employees: typing.Dict[str, float], budget: int):
        self.name = name
        self.employees = employees
        self.budget = budget

    class BudgetError(ValueError):
        def __init__(self, message):
            super(ValueError, self).__init__(message)

    def get_budget_plan(self):
        summary = 0

        for val in self.employees.values():
            summary += val
        result = self.budget - summary

        if result < 0:
            raise self.BudgetError('Custom error')

        return result

    @property
    def average_salary(self):
        average = 0
        for val in self.employees.values():
            average += val

        return '{:.2f}'.format(average / len(self.employees))

    @classmethod
    def merge_department(cls, *args):
        new_departments = sorted(sorted(list(args), key=lambda department: department.name),
                                 key=lambda department: department.average_salary, reverse=True)

        sum_salary = 0
        sum_budget = 0
        for val in new_departments:
            sum_budget += val.budget
        for val in new_departments:
            for elem in val.employees.values():
                sum_salary += elem
        if sum_budget < sum_salary:
            raise cls.BudgetError('Custom error')

        new_employee_list = {}
        for elem in new_departments:
            new_employee_list.update(elem.employees)

        new_department_list = list(map(lambda department: department.name, new_departments))
        new_department_sorted = ' - '.join(new_department_list)
        new_department = Department(new_department_sorted, new_employee_list, sum_budget)

        return new_department

    def __add__(self, other):
        return Department.merge_department(self, other)

    def __str__(self):
        return '"{} ({} - {}, {})"'.format(self.name.capitalize(), len(self.employees), self.average_salary,
                                           self.budget)

    def __or__(self, other):
        if self.get_budget_plan() < 0:
            raise self.BudgetError("1st < 0")
        elif other.get_budget_plan() < 0:
            raise self.BudgetError("2nd < 0")

        if self.get_budget_plan() >= other.get_budget_plan():
            return self.name
        else:
            return other.name


a = Department("mceo", {'nok': 5.1, 'ferf': 7.8}, 35)
b = Department("mcgyuo", {'nk': 5.1, 'fef': 7.8}, 35)
# print(a.get_budget_plan())
# print(a.average_salary)
# Department.merge_department(Department("mcgyuo", {'nk': 5.1, 'fef': 7.8}, 60),
#                            Department("mceo", {'nok': 5, 'ferf': 7.8}, 70))
# a.__add__(Department("mceo", {'nok': 5, 'ferf': 7.8}, 0))
a.__str__()
print(a.__or__(b))
