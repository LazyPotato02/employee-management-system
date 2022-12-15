from django import forms

from employee_management_sys.materials.models import Materials


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Materials
        fields = '__all__'