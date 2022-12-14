from django import forms

from employee_management_sys.cells.models import Cells


class CellForm(forms.ModelForm):
    class Meta:
        model = Cells
        fields = '__all__'