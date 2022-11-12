from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views


# Create your views here.
from employee_management_sys.employees.models import Employee


class EmployeeCreateView(views.CreateView):
    template_name = 'employee-create.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('index')
