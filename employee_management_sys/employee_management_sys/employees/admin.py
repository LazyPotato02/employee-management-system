from django.contrib import admin

# Register your models here.

# Register your models here.
from employee_management_sys.employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass

