from django.contrib import admin

from employee_management_sys.materials.models import Materials


@admin.register(Materials)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","quantity")

