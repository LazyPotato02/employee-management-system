from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# Create your views here.
from employee_management_sys.employees.forms import EmployeeForm
from employee_management_sys.employees.models import Employee


class EmployeeCreateView(LoginRequiredMixin, views.CreateView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('employee list')
    template_name = 'employees/employee-create.html'
    model = Employee
    fields = '__all__'
    success_url = reverse_lazy('employee list')


class EmployeeListView(LoginRequiredMixin, views.ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('employee list')
    model = Employee
    template_name = 'employees/employee-list.html'


class EmployeeEditView(LoginRequiredMixin, views.UpdateView):
    form_class = EmployeeForm
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('employee list')
    model = Employee
    template_name = 'employees/employee-edit.html'
    success_url = reverse_lazy('employee list')


class EmployeeDeleteView(LoginRequiredMixin, views.DeleteView):
    login_url = reverse_lazy('login')
    redirect_field_name = reverse_lazy('employee list')
    model = Employee
    template_name = 'employees/employee-delete.html'
    success_url = reverse_lazy('employee list')
