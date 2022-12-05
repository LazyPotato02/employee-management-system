from django.contrib import admin

# Register your models here.
from employee_management_sys.cells.models import Cells


@admin.register(Cells)
class CellsAdmin(admin.ModelAdmin):
    pass