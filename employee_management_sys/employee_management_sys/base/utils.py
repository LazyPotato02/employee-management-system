from employee_management_sys.employees.models import Employee


def unassign_employee_from_cell(ex):
    all_emp = Employee.objects.all()
    for em in all_emp:
        # if em in
        print(ex)
    # print(all_emp)