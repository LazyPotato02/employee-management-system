from django.contrib import admin

from employee_management_sys.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","emp_id")
    list_filter = ("cell",)
