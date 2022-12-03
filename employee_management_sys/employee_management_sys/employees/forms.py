from django import forms

from employee_management_sys.employees.models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    first_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    emp_id = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    def clean_email(self):
        return self.initial['first_name', 'last_name', 'emp_id']
